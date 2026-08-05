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

const REVIEWS_TTL = 21600;

async function fetchReviews(env, lang) {
  const key = env.GOOGLE_PLACES_API_KEY;
  const placeId = env.GOOGLE_PLACE_ID;
  if (!key || !placeId) return {reviews: []};

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
  if (!res.ok) return {reviews: []};

  const data = await res.json();
  return {
    rating: data.rating ?? null,
    total: data.userRatingCount ?? 0,
    mapsUrl: data.googleMapsUri ?? null,
    reviews: (data.reviews || [])
      .filter((r) => r.text?.text)
      .map((r) => ({
        rating: r.rating ?? 5,
        text: r.text.text,
        when: r.relativePublishTimeDescription ?? "",
        author: r.authorAttribution?.displayName ?? "",
        photo: r.authorAttribution?.photoUri ?? null
      }))
  };
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === "/api/reviews") {
      const lang = url.searchParams.get("lang") === "en" ? "en" : "tr";
      const cacheKey = new Request(`https://cache.local/reviews-${lang}`, request);
      const cache = caches.default;

      const hit = await cache.match(cacheKey);
      if (hit) return hit;

      let payload;
      try {
        payload = await fetchReviews(env, lang);
      } catch {
        payload = {reviews: []};
      }

      const response = new Response(JSON.stringify(payload), {
        headers: {
          "content-type": "application/json; charset=utf-8",
          "cache-control": `public, max-age=${REVIEWS_TTL}`
        }
      });
      if (payload.reviews.length) ctx.waitUntil(cache.put(cacheKey, response.clone()));
      return response;
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
