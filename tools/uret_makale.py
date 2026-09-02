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


AY_TR = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran",
          "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
AY_EN = ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]


def tarih_yaz(iso, tr):
    """2026-08-30T09:00:00+03:00 -> '30 Ağustos 2026' / '30 August 2026'"""
    y, a, g = int(iso[0:4]), int(iso[5:7]), int(iso[8:10])
    return f"{g} {(AY_TR if tr else AY_EN)[a-1]} {y}"


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


def alanlar_isaretini_kaldir(ust, tr):
    """Ortak şablon 'Çalışma Alanları'nı aktif işaretli tutuyor (alan sayfaları için).
    Alt kırılım sayfalarında iki başlık birden aktif görünmesin."""
    kok = "/alanlar" if tr else "/en/alanlar"
    return ust.replace(f'<a href="{kok}" class="on">', f'<a href="{kok}">')


def sayfa(m, tr, es):
    """m: üretilecek modül, es: diğer dildeki eşi (hreflang çifti onun SLUG'undan kurulur)."""
    yol = "/" + m.SLUG + "/"
    tr_slug = (m if tr else es).SLUG
    en_slug = (es if tr else m).SLUG
    tr_url = f"{SITE}/{tr_slug}/"
    en_url = f"{SITE}/{en_slug}/"
    kanonik = tr_url if tr else en_url
    # count sınırı YOK: _ust.html hem masaüstü menüsünü (.nav) hem mobil menüyü
    # (.mmenu) içeriyor; yalnızca ilkini işaretlemek mobilde vurguyu düşürüyordu.
    ust = (UST.replace('<a href="/yazilar">', '<a href="/yazilar" class="on">') if tr
           else en_parca("ust").replace('<a href="/en/yazilar">', '<a href="/en/yazilar" class="on">'))
    alt = ALT if tr else en_parca("alt")
    ust = alanlar_isaretini_kaldir(ust, tr)

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
        # tablo: modül TABLO_BOLUM tanımlamışsa o bölümün sonuna eklenir
        if i == getattr(m, "TABLO_BOLUM", -1):
            ic += getattr(m, "TABLO", TABLO_TR if tr else TABLO_EN)
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
       "image": SITE + getattr(m, "GORSEL", GORSEL),
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
    tarih_gorunen = tarih_yaz(m.TARIH, tr)
    gorsel = getattr(m, "GORSEL", GORSEL)
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
<meta property="og:image" content="{SITE}{gorsel}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{kacis(m.H1)}" />
<meta name="twitter:description" content="{kacis(m.DESC)}" />
<meta name="twitter:image" content="{SITE}{gorsel}" />
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


# (türkçe modül, ingilizce modül) çiftleri — yeni makale buraya eklenir
CIFTLER = [("makale_tr", "makale_en"),
           ("makale_cocuk_tr", "makale_cocuk_en"),
           ("makale_icra_tr", "makale_icra_en"),
           ("makale_hagb_tr", "makale_hagb_en"),
           ("makale_usul_tr", "makale_usul_en"),
           ("makale_arac_tr", "makale_arac_en"),
           ("makale_miras_tr", "makale_miras_en")]


def uret():
    import importlib
    for tr_ad, en_ad in CIFTLER:
        mt, me = importlib.import_module(tr_ad), importlib.import_module(en_ad)
        for m, tr, es in ((mt, True, me), (me, False, mt)):
            d = PUB / m.SLUG
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(sayfa(m, tr, es))
            print("yazildi:", m.SLUG + "/index.html")


if __name__ == "__main__":
    uret()
