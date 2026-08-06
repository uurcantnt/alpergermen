const SITEMAP = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://alpergermen.av.tr/</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/alanlar</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/kurumsal</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/yazilar</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/sss</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/iletisim</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/alanlar</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/kurumsal</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/yazilar</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/sss</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://alpergermen.av.tr/en/iletisim</loc>
    <lastmod>2026-08-06</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>`;

const ROBOTS = `User-agent: *
Allow: /

Sitemap: https://alpergermen.av.tr/sitemap.xml
`;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

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
