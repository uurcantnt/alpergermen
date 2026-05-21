export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.pathname === "/sitemap.xml") {
    const xml = `<?xml version="1.0" encoding="UTF-8"?>
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

    return new Response(xml, {
      headers: {
        "content-type": "application/xml; charset=utf-8",
        "cache-control": "public, max-age=3600"
      }
    });
  }

  return context.next();
}
