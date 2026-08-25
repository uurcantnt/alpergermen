# -*- coding: utf-8 -*-
"""Makale sayfalarını üretir (TR + EN) ve /yazilar listelerini günceller."""
import html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

KOK = pathlib.Path(__file__).resolve().parent.parent
PUB = KOK / "public"
SITE = "https://alpergermen.av.tr"
GORSEL = "/assets/avukat.png"          # /assets içinde gerçekten var
UST = (KOK / "tools/_ust.html").read_text()
ALT = (KOK / "tools/_alt.html").read_text()


def en_parca(hangi):
    k = (PUB / "en/alanlar.html").read_text()
    if hangi == "ust":
        return k[k.index('<div class="topbar">'):k.index('<section')]
    p = k[k.index('<footer class="footer">'):k.index('</body>')]
    return re.sub(r'\s*<script src="/main(-en)?\.js" defer></script>\s*$', '\n', p)


def kacis(t):
    """Metin kaçışı — içerideki <a> etiketleri korunur."""
    korunan = re.findall(r'<a href="[^"]*">.*?</a>', t)
    for i, k in enumerate(korunan):
        t = t.replace(k, f"@@A{i}@@", 1)
    t = html.escape(t, quote=False)
    for i, k in enumerate(korunan):
        t = t.replace(f"@@A{i}@@", k, 1)
    return t


TABLO_TR = """
      <div class="tablo-sar">
      <table class="lp-tablo">
        <caption>Kesinleşmemiş dosya ile kesinleşmiş dosya arasındaki fark</caption>
        <thead><tr><th scope="col">Ölçüt</th><th scope="col">Kesinleşmemiş dosya</th><th scope="col">Kesinleşmiş / infaz aşamasındaki dosya</th></tr></thead>
        <tbody>
          <tr><th scope="row">Zararı giderme şartı</th><td>Aranmaz</td><td>Aranır; zarar tamamen giderilmelidir</td></tr>
          <tr><th scope="row">Süre</th><td>Kanun yolu aşamasına bağlıdır</td><td>Mahkemenin ihtarından itibaren altı ay</td></tr>
          <tr><th scope="row">Sonuç</th><td>Fiil kapsamdaysa ceza yarı oranında indirilir</td><td>Zarar giderilirse TCK m.168/2 uygulanabilir</td></tr>
          <tr><th scope="row">İnfaza etkisi</th><td>Dosya derdest olduğundan infaz söz konusu değildir</td><td>Zarar tamamen giderilinceye kadar infaz ertelenemez veya durdurulamaz</td></tr>
        </tbody>
      </table>
      </div>"""

TABLO_EN = """
      <div class="tablo-sar">
      <table class="lp-tablo">
        <caption>Difference between a pending file and a final conviction</caption>
        <thead><tr><th scope="col">Criterion</th><th scope="col">File not yet final</th><th scope="col">Final conviction / execution stage</th></tr></thead>
        <tbody>
          <tr><th scope="row">Compensation required</th><td>Not required</td><td>Required; the loss must be made good in full</td></tr>
          <tr><th scope="row">Time limit</th><td>Depends on the appellate stage</td><td>Six months from the court's formal notice</td></tr>
          <tr><th scope="row">Result</th><td>If the act qualifies, the sentence is halved</td><td>If the loss is made good, Article 168/2 may apply</td></tr>
          <tr><th scope="row">Effect on execution</th><td>No execution, as the file is still pending</td><td>Execution cannot be postponed or suspended until the loss is fully made good</td></tr>
        </tbody>
      </table>
      </div>"""


def sayfa(m, tr):
    yol = "/" + m.SLUG + "/"
    tr_url = f"{SITE}/{m.SLUG}/" if tr else f"{SITE}/" + m.SLUG.replace("en/yazilar/tck-158-4-account-lending-sentence-reduction", "yazilar/tck-158-4-iban-kullandirma-ceza-indirimi") + "/"
    en_url = f"{SITE}/en/yazilar/tck-158-4-account-lending-sentence-reduction/"
    tr_url = f"{SITE}/yazilar/tck-158-4-iban-kullandirma-ceza-indirimi/"
    kanonik = tr_url if tr else en_url
    ust = (UST if tr else en_parca("ust")).replace('<a href="/yazilar">', '<a href="/yazilar" class="on">', 1) \
        if tr else en_parca("ust").replace('<a href="/en/yazilar">', '<a href="/en/yazilar" class="on">', 1)
    alt = ALT if tr else en_parca("alt")

    govde = []
    for i, (h2, paragraflar) in enumerate(m.BOLUMLER):
        ic = ""
        for p in paragraflar:
            if p == "@LISTE@":
                ic += ('\n      <ol class="makale-adim">'
                       + "".join(f"<li>{kacis(a)}</li>" for a in m.ADIMLAR)
                       + "</ol>")
            else:
                ic += f"\n      <p>{kacis(p)}</p>"
        # tabloyu 6. bölümün (kesinleşmiş dosyalar) sonuna koy
        if i == 5:
            ic += (TABLO_TR if tr else TABLO_EN)
        govde.append(f'\n  <section class="section tight lp-blok">\n    <div class="wrap lp-wrap">'
                     f'\n      <h2>{kacis(h2)}</h2>{ic}\n    </div>\n  </section>')

    sss_bas = "Sık sorulan sorular" if tr else "Frequently asked questions"
    sss_giris = ('Aşağıdaki sorular bu düzenlemeye özgüdür; büroya sıkça yöneltilen genel sorular '
                 '<a href="/sss">sık sorulan sorular sayfasında</a> yer alır.'
                 if tr else
                 'The questions below concern this provision; more general questions are answered on '
                 'the <a href="/en/sss">frequently asked questions page</a>.')
    sss_html = "".join(
        f'\n      <div class="qa">\n        <button class="qa-q">'
        f'<span class="qa-mark">{i+1:02d}</span><span>{kacis(q)}</span>'
        f'<span class="qa-ico"></span></button>'
        f'\n        <div class="qa-a"><div class="qa-a-inner"><p>{kacis(a)}</p></div></div>\n      </div>'
        for i, (q, a) in enumerate(m.SSS))
    govde.append(f'''
  <section class="section tight lp-blok">
    <div class="wrap lp-wrap">
      <h2>{sss_bas}</h2>
      <p>{sss_giris}</p>
      <div class="lp-sss">{sss_html}
      </div>
    </div>
  </section>''')

    kapanis = "".join(f"\n      <p>{kacis(p)}</p>" for p in m.KAPANIS)
    uyari_bas = "Yasal uyarı" if tr else "Legal notice"
    govde.append(f'''
  <section class="section tight lp-blok">
    <div class="wrap lp-wrap">{kapanis}
      <aside class="yasal-uyari" aria-label="{uyari_bas}">
        <b>{uyari_bas}</b>
        <p>{kacis(m.UYARI)}</p>
      </aside>
    </div>
  </section>''')

    kirilim2 = "Hukuki Makaleler" if tr else "Legal Articles"
    graf = {"@context": "https://schema.org", "@graph": [
      {"@type": "BlogPosting", "@id": kanonik + "#article",
       "headline": m.H1, "description": m.DESC, "url": kanonik,
       "inLanguage": "tr-TR" if tr else "en",
       "image": SITE + GORSEL,
       "datePublished": m.TARIH, "dateModified": m.TARIH,
       "articleSection": m.ARTICLE_SECTION,
       "mainEntityOfPage": {"@type": "WebPage", "@id": kanonik},
       "author": {"@id": SITE + "/#alpergermen"},
       "publisher": {"@id": SITE + "/#legalservice"},
       "isPartOf": {"@id": SITE + "/yazilar#page"}},
      {"@type": "BreadcrumbList", "@id": kanonik + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana Sayfa" if tr else "Home",
         "item": SITE + ("/" if tr else "/en/")},
        {"@type": "ListItem", "position": 2, "name": kirilim2,
         "item": SITE + ("/yazilar" if tr else "/en/yazilar")},
        {"@type": "ListItem", "position": 3, "name": m.H1, "item": kanonik}]},
      {"@type": "FAQPage", "@id": kanonik + "#faq",
       "inLanguage": "tr-TR" if tr else "en",
       "mainEntity": [{"@type": "Question", "name": q,
                       "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m.SSS]},
      {"@type": "Person", "@id": SITE + "/#alpergermen",
       "name": "Alper Germen", "jobTitle": "Avukat" if tr else "Attorney",
       "worksFor": {"@id": SITE + "/#legalservice"}},
    ]}

    ana = "Ana Sayfa" if tr else "Home"
    tarih_gorunen = "25 Ağustos 2026" if tr else "25 August 2026"
    rg_metin = ("Kanunun Resmî Gazete'de yayımlanan metni" if tr
                else "the text as published in the Official Gazette")
    kaynak_cumle = (f'Düzenlemenin resmî metni için '
                    f'<a href="{m.RG_LINK}" target="_blank" rel="noopener">{rg_metin}</a> '
                    f'incelenebilir.' if tr else
                    f'The provision can be consulted in '
                    f'<a href="{m.RG_LINK}" target="_blank" rel="noopener">{rg_metin}</a>.')

    return f"""<!DOCTYPE html>
<html lang="{'tr' if tr else 'en'}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{kacis(m.TITLE)}</title>
<meta name="description" content="{kacis(m.DESC)}" />
<link rel="canonical" href="{kanonik}" />
<link rel="alternate" hreflang="tr" href="{tr_url}" />
<link rel="alternate" hreflang="en" href="{en_url}" />
<link rel="alternate" hreflang="x-default" href="{tr_url}" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="{'Av. Alper Germen Hukuk Bürosu' if tr else 'Alper Germen Law Office'}" />
<meta property="og:locale" content="{'tr_TR' if tr else 'en_US'}" />
<meta property="og:title" content="{kacis(m.H1)}" />
<meta property="og:description" content="{kacis(m.DESC)}" />
<meta property="og:url" content="{kanonik}" />
<meta property="og:image" content="{SITE}{GORSEL}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{kacis(m.H1)}" />
<meta name="twitter:description" content="{kacis(m.DESC)}" />
<meta name="twitter:image" content="{SITE}{GORSEL}" />
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
    <div class="crumbs"><a href="{'/' if tr else '/en/'}">{ana}</a> — <a href="{'/yazilar' if tr else '/en/yazilar'}">{kirilim2}</a> — <span>{kacis(m.H1)}</span></div>
    <p class="kicker"><span class="no">—</span> {kacis(m.KICKER)}</p>
    <h1>{kacis(m.H1)}</h1>
    <p class="makale-tarih"><time datetime="{m.TARIH}">{tarih_gorunen}</time></p>
    <p class="lp-lead">{kacis(m.OZET)}</p>
  </div>
</section>

  <section class="section tight lp-blok">
    <div class="wrap lp-wrap">{"".join(f'{chr(10)}      <p>{kacis(p)}</p>' for p in m.GIRIS)}
      <p>{kaynak_cumle}</p>
    </div>
  </section>
{"".join(govde)}

{alt}
<script src="/{'main.js' if tr else 'main-en.js'}" defer></script>
</body>
</html>
"""


def uret():
    import makale_tr, makale_en
    for m, tr in ((makale_tr, True), (makale_en, False)):
        d = PUB / m.SLUG
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(sayfa(m, tr))
        print("yazildi:", m.SLUG + "/index.html")


if __name__ == "__main__":
    uret()
