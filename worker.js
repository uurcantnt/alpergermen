const SITEMAP = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://alpergermen.av.tr/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/alanlar</loc>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/kurumsal</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/yazilar</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/sss</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/iletisim</loc>
    <changefreq>yearly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/alanlar</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/kurumsal</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/yazilar</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/sss</loc>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/iletisim</loc>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>`;

const ROBOTS = `User-agent: *
Allow: /

Sitemap: https://alpergermen.av.tr/sitemap.xml
`;

/* Google Places "reviews" alanı en pahalı SKU'yu (Enterprise + Atmosphere)
   tetikler ve ayda yalnızca 1.000 çağrı ücretsizdir. Bu yüzden başarılı yanıt
   uzun, başarısız yanıt kısa süre önbelleğe alınır — hatalı bir yapılandırma
   her sayfa ziyaretinde Google'a çağrı yapılmasına yol açmasın. */
const REVIEWS_TTL_OK = 86400;
const REVIEWS_TTL_FAIL = 600;

async function fetchReviews(env, lang) {
  const key = env.GOOGLE_PLACES_API_KEY;
  const placeId = env.GOOGLE_PLACE_ID;
  if (!key || !placeId) return {reviews: [], error: "missing_config"};

  const endpoint =
    `https://places.googleapis.com/v1/places/${encodeURIComponent(placeId)}` +
    `?languageCode=${lang === "en" ? "en" : "tr"}`;

  const res = await fetch(endpoint, {
    headers: {
      "X-Goog-Api-Key": key,
      "X-Goog-FieldMask":
        "rating,userRatingCount,googleMapsUri,reviews.rating,reviews.text,reviews.relativePublishTimeDescription,reviews.authorAttribution"
    }
  });
  /* Durum kodu teşhis için döndürülür; Google'ın hata gövdesi anahtar
     parçası içerebildiğinden dışarı sızdırılmaz. */
  if (!res.ok) return {reviews: [], error: `http_${res.status}`};

  const data = await res.json();
  const reviews = (data.reviews || [])
    .filter((r) => r.text?.text)
    .map((r) => ({
      rating: r.rating ?? 5,
      text: r.text.text,
      when: r.relativePublishTimeDescription ?? "",
      author: r.authorAttribution?.displayName ?? "",
      photo: r.authorAttribution?.photoUri ?? null
    }));

  return {
    rating: data.rating ?? null,
    total: data.userRatingCount ?? 0,
    mapsUrl: data.googleMapsUri ?? null,
    reviews,
    ...(reviews.length ? {} : {error: "no_reviews"})
  };
}

/* Yorum taşımayan yanıtlar kısa ömürlüdür; yanlış yapılandırma tarayıcıda
   bir gün boyunca çakılı kalmasın. */
function ttlFor(payload) {
  return payload?.reviews?.length ? REVIEWS_TTL_OK : REVIEWS_TTL_FAIL;
}

/* cdn-cache-control olmadan Cloudflare edge'i bu yanıtı kendi varsayılan
   süresiyle (4 saat) tutuyor ve kısa ömürlü hata yanıtlarını oraya çiviliyordu;
   secret düzeltildikten sonra bile eski boş yanıt servis ediliyordu. */
function reviewsResponse(body, ttl) {
  return new Response(body, {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": `public, max-age=${ttl}`,
      "cdn-cache-control": `public, max-age=${ttl}`
    }
  });
}

function parsePayload(body) {
  try {
    return JSON.parse(body);
  } catch {
    return null;
  }
}

async function handleReviews(request, env, ctx) {
  const lang = new URL(request.url).searchParams.get("lang") === "en" ? "en" : "tr";
  const cacheName = `reviews-${lang}`;
  const kv = env.REVIEWS_KV;

  /* KV bağlıysa önbellek tüm dünyada tektir. Değilse Cache API'ye düşülür;
     o önbellek her Cloudflare lokasyonunda ayrı olduğundan aynı içerik için
     Google'a lokasyon sayısı kadar çağrı gider. */
  if (kv) {
    const hit = await kv.get(cacheName);
    const cached = hit && parsePayload(hit);
    if (cached) return reviewsResponse(hit, ttlFor(cached));
  }

  const cacheKey = new Request(`https://cache.local/${cacheName}`);
  if (!kv) {
    const hit = await caches.default.match(cacheKey);
    if (hit) return hit;
  }

  let payload;
  try {
    payload = await fetchReviews(env, lang);
  } catch {
    payload = {reviews: [], error: "fetch_failed"};
  }

  const body = JSON.stringify(payload);
  const ttl = ttlFor(payload);
  const response = reviewsResponse(body, ttl);

  if (kv) {
    ctx.waitUntil(kv.put(cacheName, body, {expirationTtl: ttl}));
  } else {
    ctx.waitUntil(caches.default.put(cacheKey, response.clone()));
  }
  return response;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === "/api/reviews") {
      return handleReviews(request, env, ctx);
    }

    if (url.pathname === "/sitemap.xml") {
      return new Response(SITEMAP, {
        headers: {
          "content-type": "application/xml; charset=utf-8",
          "cache-control": "public, max-age=3600"
        }
      });
    }

    if (url.pathname === "/robots.txt") {
      return new Response(ROBOTS, {
        headers: {
          "content-type": "text/plain; charset=utf-8",
          "cache-control": "public, max-age=86400"
        }
      });
    }

    return env.ASSETS.fetch(request);
  }
};
