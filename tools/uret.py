# -*- coding: utf-8 -*-
"""Hizmet alanı açılış sayfalarını üretir (TR + EN).

Sayfa iskeleti mevcut sayfalardan alınan ortak parçalarla kurulur;
böylece topbar, header, menü ve footer tek kaynaktan gelir.
"""
import html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

KOK = pathlib.Path(__file__).resolve().parent.parent
PUB = KOK / "public"
SITE = "https://alpergermen.av.tr"

UST = (KOK / "tools/_ust.html").read_text()
ALT = (KOK / "tools/_alt.html").read_text()


def menu_isaretle(parca, aktif="/alanlar"):
    """Üst menüde 'Çalışma Alanları' işaretini kaldırır — alan sayfaları alt kırılım."""
    return parca.replace('<a href="/alanlar" class="on">', '<a href="/alanlar">')


def en_cevir(parca):
    """Ortak parçanın İngilizce sayfalardaki karşılığını alır."""
    kaynak = (PUB / "en/alanlar.html").read_text()
    if parca is UST:
        bas = kaynak.index('<div class="topbar">')
        son = kaynak.index('<section')
        return kaynak[bas:son]
    bas = kaynak.index('<footer class="footer">')
    parca = kaynak[bas:kaynak.index('</body>')]
    # script şablonda ayrıca eklendiği için burada kırpılır (çift yükleme olmasın)
    return re.sub(r'\s*<script src="/main(-en)?\.js" defer></script>\s*$', '\n', parca)


def kacis(t):
    return html.escape(t, quote=False)


def sayfa(slug, v, lang):
    tr = lang == "tr"
    yol = f"/{slug}/"
    tr_url, en_url = f"{SITE}{yol}", f"{SITE}/en{yol}"
    kanonik = tr_url if tr else en_url
    ust = UST if tr else en_cevir(UST)
    alt = ALT if tr else en_cevir(ALT)
    ust = menu_isaretle(ust)

    # --- gövde bölümleri ---
    bolumler = []
    for i, (h2, paragraflar) in enumerate(v["bolumler"]):
        ic = "".join(f"\n      <p>{kacis(p)}</p>" for p in paragraflar)
        bolumler.append(
            f'\n  <section class="section tight lp-blok">\n    <div class="wrap lp-wrap">'
            f'\n      <h2>{kacis(h2)}</h2>{ic}\n    </div>\n  </section>')

    sss_html = "".join(
        f'\n      <div class="qa">\n        <button class="qa-q">'
        f'<span class="qa-mark">{i+1:02d}</span><span>{kacis(s)}</span>'
        f'<span class="qa-ico"></span></button>'
        f'\n        <div class="qa-a"><div class="qa-a-inner"><p>{kacis(c)}</p></div></div>'
        f'\n      </div>'
        for i, (s, c) in enumerate(v["sss"]))

    ilgili_html = "".join(
        f'<a class="ta" href="{u if tr else "/en" + u}"><h4>{kacis(b)}</h4></a>'
        for u, b in v["ilgili"])

    # --- JSON-LD ---
    kirilim = "Çalışma Alanları" if tr else "Practice Areas"
    graf = {
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "BreadcrumbList", "@id": kanonik + "#breadcrumb",
         "itemListElement": [
           {"@type": "ListItem", "position": 1,
            "name": "Ana Sayfa" if tr else "Home",
            "item": SITE + ("/" if tr else "/en/")},
           {"@type": "ListItem", "position": 2, "name": kirilim,
            "item": SITE + ("/alanlar" if tr else "/en/alanlar")},
           {"@type": "ListItem", "position": 3, "name": v["h1"], "item": kanonik},
         ]},
        {"@type": "FAQPage", "@id": kanonik + "#faq",
         "mainEntity": [
           {"@type": "Question", "name": s,
            "acceptedAnswer": {"@type": "Answer", "text": c}}
           for s, c in v["sss"]]},
        {"@type": "Service", "@id": kanonik + "#service",
         "name": v["h1"], "serviceType": v["kicker"],
         "provider": {"@id": SITE + "/#legalservice"},
         "areaServed": [{"@type": "City", "name": "Antalya"},
                        {"@type": "AdministrativeArea", "name": "Konyaaltı"}],
         "url": kanonik},
      ]}

    tel = "+90 553 772 76 01"
    cta_baslik = "Dosyanız için randevu alın" if tr else "Book a meeting for your case"
    cta_metin = ("Görüşme öncesinde elinizdeki belgeleri iletmeniz, değerlendirmenin daha "
                 "isabetli yapılmasını sağlar." if tr else
                 "Sharing your documents before the meeting allows for a more accurate assessment.")
    tum_alanlar = "Tüm çalışma alanları" if tr else "All practice areas"
    ilgili_bas = "İlgili alanlar" if tr else "Related areas"
    sss_bas = "Sıkça Sorulan Sorular" if tr else "Frequently Asked Questions"
    ana = "Ana Sayfa" if tr else "Home"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{kacis(v['title'])}</title>
<meta name="description" content="{kacis(v['desc'])}" />
<link rel="canonical" href="{kanonik}" />
<link rel="alternate" hreflang="tr" href="{tr_url}" />
<link rel="alternate" hreflang="en" href="{en_url}" />
<link rel="alternate" hreflang="x-default" href="{tr_url}" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="{'Av. Alper Germen Hukuk Bürosu' if tr else 'Alper Germen Law Office'}" />
<meta property="og:locale" content="{'tr_TR' if tr else 'en_US'}" />
<meta property="og:locale:alternate" content="{'en_US' if tr else 'tr_TR'}" />
<meta property="og:title" content="{kacis(v['title'])}" />
<meta property="og:description" content="{kacis(v['desc'])}" />
<meta property="og:url" content="{kanonik}" />
<meta property="og:image" content="{SITE}/assets/avukat.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{kacis(v['title'])}" />
<meta name="twitter:description" content="{kacis(v['desc'])}" />
<meta name="twitter:image" content="{SITE}/assets/avukat.png" />
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{json.dumps(graf, ensure_ascii=False, indent=2)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>

{ust}
<section class="page-head">
  <div class="wrap">
    <div class="crumbs"><a href="{'/' if tr else '/en/'}">{ana}</a> — <a href="{'/alanlar' if tr else '/en/alanlar'}">{kirilim}</a> — <span>{kacis(v['h1'])}</span></div>
    <p class="kicker"><span class="no">—</span> {kacis(v['kicker'])}</p>
    <h1>{kacis(v['h1'])}</h1>
    <p class="lp-lead">{kacis(v['lead'])}</p>
    <div class="lp-actions">
      <a class="btn-solid" href="tel:+905537727601">{tel}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a class="btn-ghost" href="{'/iletisim' if tr else '/en/iletisim'}">{'İletişim ve Randevu' if tr else 'Contact & Appointment'}</a>
    </div>
  </div>
</section>
{"".join(bolumler)}

  <section class="section tight lp-blok">
    <div class="wrap lp-wrap">
      <h2>{sss_bas}</h2>
      <div class="lp-sss">{sss_html}
      </div>
    </div>
  </section>

  <section class="section tight lp-blok">
    <div class="wrap lp-wrap">
      <h2>{ilgili_bas}</h2>
      <div class="teaser-areas lp-ilgili">{ilgili_html}</div>
      <p style="margin-top:26px"><a class="link-more" href="{'/alanlar' if tr else '/en/alanlar'}">{tum_alanlar}
        <svg viewBox="0 0 24 24" width="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></p>
    </div>
  </section>

  <section class="section faq bordered lp-cta">
    <div class="wrap">
      <div class="faq-aside">
        <p class="kicker"><span class="no">—</span> {'İletişim' if tr else 'Contact'}</p>
        <h2 class="h-section">{cta_baslik}</h2>
        <p>{cta_metin}</p>
        <div class="lp-actions" style="margin-top:28px">
          <a class="btn-solid" href="tel:+905537727601">{tel}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a class="btn-ghost" href="{'/iletisim' if tr else '/en/iletisim'}">{'İletişim ve Randevu' if tr else 'Contact & Appointment'}</a>
        </div>
      </div>
    </div>
  </section>

{alt}
<script src="/{'main.js' if tr else 'main-en.js'}" defer></script>
</body>
</html>
"""


def uret():
    from icerik_tr import ALANLAR as TR
    from icerik_en import ALANLAR as EN
    n = 0
    for slug, v in TR.items():
        d = PUB / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(sayfa(slug, v, "tr"))
        n += 1
    for slug, v in EN.items():
        d = PUB / "en" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(sayfa(slug, v, "en"))
        n += 1
    print(f"{n} sayfa uretildi")


if __name__ == "__main__":
    uret()
