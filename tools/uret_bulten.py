# -*- coding: utf-8 -*-
"""Mevzuat bülteni sayfasını üretir (TR + EN).

Bültende yalnızca Resmî Gazete'de yayımlanmış bir kanun değişikliğini konu alan
yazılar listelenir. Yazılar ayrıca kendi hukuk dalıyla /yazilar sayfasında da
görünmeye devam eder; bülten ikinci bir giriş noktasıdır.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from uret_makale import PUB, SITE, UST, ALT, en_parca

# (yol, künye, başlık, özet, alan) — yeniden eskiye
KAYIT_TR = [
 ("/yazilar/tck-31-cocuklarin-ceza-sorumlulugu/",
  "7593 sayılı Kanun — Resmî Gazete, 18 Ağustos 2026 (S. 33344)", "2026-08-30", "30 Ağustos 2026",
  "TCK 31: Çocukların Ceza Sorumluluğunda 2026 Değişikliği",
  "12-15 ve 15-18 yaş gruplarında ceza aralıkları yükseltildi; kasten öldürme ve neticesi sebebiyle "
  "ağırlaşmış yaralama suçlarında yaş indiriminin uygulanmamasına imkân tanıyan fıkra eklendi. "
  "Lehe kanun ilkesi gereği 18 Ağustos 2026 öncesi fiillere uygulanmaz.", "Ceza Hukuku"),
 ("/yazilar/ortakligin-giderilmesi-ihalesinde-yeni-kurallar/",
  "7589 sayılı Kanun — Resmî Gazete, 31 Temmuz 2026 (S. 33326)", "2026-08-30", "30 Ağustos 2026",
  "Ortaklığın Giderilmesi İhalesinde Yeni Kurallar",
  "İİK m.114 değişti: miras yoluyla edinilen taşınmazlarda birinci artırma yalnızca malik mirasçılar "
  "arasında yapılacak ve teklif eşiği muhammen kıymetin yüzde yüzü olacak. Geçiş ölçütü artırma "
  "ilanının tarihidir.", "İcra ve İflas Hukuku"),
 ("/yazilar/tck-158-4-iban-kullandirma-ceza-indirimi/",
  "7589 sayılı Kanun — Resmî Gazete, 31 Temmuz 2026 (S. 33326)", "2026-08-25", "25 Ağustos 2026",
  "TCK 158/4: Hesabını Kullandıranlara Ceza İndirimi",
  "Dolandırıcılığa katılımı banka hesabını, kartını veya hesabın kullanılmasını sağlayan bilgileri "
  "vermekle sınırlı kalan kişilerin cezası yarı oranında indirilir. Kesinleşmiş ve derdest dosyalar "
  "arasındaki fark ile altı aylık süre ayrıca ele alınıyor.", "Ceza Hukuku"),
]

KAYIT_EN = [
 ("/en/yazilar/criminal-responsibility-of-minors-turkey/",
  "Law no. 7593 — Official Gazette, 18 August 2026 (issue 33344)", "2026-08-30", "30 August 2026",
  "Article 31 TPC: The 2026 Change to the Criminal Responsibility of Minors",
  "Sentence ranges rose in both the 12-15 and 15-18 age bands, and a new paragraph allows the age "
  "reduction to be disapplied in cases of intentional killing and injury aggravated by result. It "
  "does not apply to acts committed before 18 August 2026.", "Criminal Law"),
 ("/en/yazilar/partition-auctions-new-rules/",
  "Law no. 7589 — Official Gazette, 31 July 2026 (issue 33326)", "2026-08-30", "30 August 2026",
  "New Rules for Partition Auctions Under Law No. 7589",
  "Article 114 of the Enforcement Law changed: for property acquired by inheritance the first auction "
  "is held among the co-owning heirs alone, at a bid threshold of the full appraised value. The "
  "transitional test is the date of the auction advertisement.", "Enforcement and Bankruptcy Law"),
 ("/en/yazilar/tck-158-4-account-lending-sentence-reduction/",
  "Law no. 7589 — Official Gazette, 31 July 2026 (issue 33326)", "2026-08-25", "25 August 2026",
  "Article 158/4 TPC: Reduced Sentences for Lending a Bank Account",
  "Where participation in fraud was limited to handing over a bank account, a card or the information "
  "needed to use an account, the sentence is halved. The difference between pending and final files "
  "and the six-month window are examined.", "Criminal Law"),
]

METIN = {
 True: dict(
   url="https://alpergermen.av.tr/bulten/", no="05",
   title="Mevzuat Bülteni | Av. Alper Germen, Antalya",
   desc="Resmî Gazete'de yayımlanan kanun değişikliklerinin uygulamaya etkisi: yürürlük tarihleri, "
        "geçiş hükümleri ve hangi dosyaları ilgilendirdiği tek sayfada.",
   ana="Ana Sayfa", kirilim="Bülten", h1_a="Mevzuat", h1_b="bülteni.",
   lead="Resmî Gazete'de yayımlanan kanun değişikliklerinden büronun çalışma alanlarını "
        "ilgilendirenler, tarih sırasıyla burada derlenir. Her başlıkta düzenlemenin hangi kanunla "
        "geldiği, Resmî Gazete tarihi ve sayısı, yürürlük tarihi ve varsa geçiş hükmü belirtilir.",
   h2="Yayımlanan düzenlemeler",
   giris="Bülten, mevzuat takibini tek bir yerde toplamak için hazırlanmıştır. Aşağıdaki başlıklar "
         "aynı zamanda ilgili hukuk dalıyla birlikte <a href=\"/yazilar\">Yazılar</a> sayfasında da "
         "yer alır; buradaki sıralama yayım tarihine göredir.",
   h2b="Bülten nasıl okunmalı?",
   nasil=["Bir kanun değişikliğinin devam eden bir dosyaya etkisi, çoğu zaman değişikliğin kendisi "
          "kadar <strong>geçiş hükmüne</strong> bağlıdır. Usul hükümlerinde ölçüt genellikle davanın "
          "açıldığı tarih; ceza hükümlerinde <strong>fiilin işlendiği tarih</strong>; icra "
          "işlemlerinde ise çoğu zaman <strong>artırma ilanının tarihidir</strong>.",
          "Bu nedenle her yazıda düzenlemenin yürürlük tarihi ve geçiş kuralı ayrıca belirtilmiştir. "
          "Bültendeki açıklamalar genel bilgilendirme amaçlıdır ve hukuki danışmanlık niteliği "
          "taşımaz; bir düzenlemenin somut dosyaya etkisi dosyanın tarihi ve bulunduğu aşama "
          "birlikte değerlendirilerek belirlenir."],
   oku="Yazıyı oku →", alan="İlgili alan:", ad="Mevzuat Bülteni", lang="tr", locale="tr_TR",
   nav_es=('<a href="/yazilar">Yazılar</a>', '<a href="/yazilar">Yazılar</a><a href="/bulten/" class="on">Bülten</a>')),
 False: dict(
   url="https://alpergermen.av.tr/en/legal-updates/", no="05",
   title="Legal Updates | Av. Alper Germen, Antalya",
   desc="Amendments published in the Turkish Official Gazette and their effect in practice: dates of "
        "entry into force, transitional rules and the files they concern.",
   ana="Home", kirilim="Legal Updates", h1_a="Legislative", h1_b="bulletin.",
   lead="Amendments published in the Official Gazette that bear on the office's fields of work are "
        "collected here in date order. Each entry states the law that introduced the change, the date "
        "and issue of the Official Gazette, the date of entry into force and any transitional rule.",
   h2="Published amendments",
   giris="The bulletin brings legislative tracking together in one place. The entries below also "
         "appear, with their field of law, in the <a href=\"/en/yazilar\">Articles</a> section; the "
         "order here follows the date of publication.",
   h2b="How to read the bulletin",
   nasil=["The effect of an amendment on a pending file often depends as much on the "
          "<strong>transitional rule</strong> as on the change itself. For procedural provisions the "
          "test is usually the date proceedings were issued; in criminal matters the <strong>date of "
          "the act</strong>; and in enforcement matters most often the <strong>date of the auction "
          "advertisement</strong>.",
          "Each article therefore states the date of entry into force and the transitional rule "
          "separately. The bulletin is for general information only and does not constitute legal "
          "advice; the effect of an amendment on a particular file is determined by looking at the "
          "date of the file together with the stage it has reached."],
   oku="Read the article →", alan="Related area:", ad="Legislative Bulletin", lang="en",
   locale="en_US",
   nav_es=('<a href="/en/yazilar">Articles</a>',
           '<a href="/en/yazilar">Articles</a><a href="/en/legal-updates/" class="on">Legal Updates</a>')),
}

TR_URL = "https://alpergermen.av.tr/bulten/"
EN_URL = "https://alpergermen.av.tr/en/legal-updates/"


def sayfa(tr):
    M = METIN[tr]
    kayitlar = KAYIT_TR if tr else KAYIT_EN
    ust = (UST if tr else en_parca("ust"))
    alt = (ALT if tr else en_parca("alt"))
    # menüde Yazılar'ı bırak, yanına Bülten ekle ve işaretle
    eski_nav, yeni_nav = M["nav_es"]
    ust = ust.replace(eski_nav, yeni_nav).replace(
        eski_nav.replace('<a href', '<a class="" href'), yeni_nav)
    kartlar = "".join(
        f'\n      <a class="art makale-kart" href="{yol}">'
        f'<span class="art-tag">{kunye}</span>'
        f'<h3>{baslik}</h3>'
        f'<p class="art-tarih"><time datetime="{iso}">{gorunen}</time></p>'
        f'<p>{ozet}</p>'
        f'<span class="art-read">{M["alan"]} {alan} · {M["oku"]}</span></a>'
        for yol, kunye, iso, gorunen, baslik, ozet, alan in kayitlar)
    nasil = "".join(f'\n      <p>{p}</p>' for p in M["nasil"])

    graf = {"@context": "https://schema.org", "@graph": [
      {"@type": "CollectionPage", "@id": M["url"] + "#page", "url": M["url"], "name": M["ad"],
       "description": M["desc"], "inLanguage": "tr-TR" if tr else "en",
       "isPartOf": {"@id": SITE + ("/#website" if tr else "/en/#website")},
       "mainEntity": {"@type": "ItemList", "itemListElement": [
           {"@type": "ListItem", "position": i + 1, "url": SITE + k[0], "name": k[4]}
           for i, k in enumerate(kayitlar)]}},
      {"@type": "BreadcrumbList", "@id": M["url"] + "#breadcrumb", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": M["ana"], "item": SITE + ("/" if tr else "/en/")},
          {"@type": "ListItem", "position": 2, "name": M["ad"], "item": M["url"]}]}]}

    return f"""<!DOCTYPE html>
<html lang="{M["lang"]}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{M["title"]}</title>
<meta name="description" content="{M["desc"]}" />
<link rel="canonical" href="{M["url"]}" />
<link rel="alternate" hreflang="tr" href="{TR_URL}" />
<link rel="alternate" hreflang="en" href="{EN_URL}" />
<link rel="alternate" hreflang="x-default" href="{TR_URL}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{'Av. Alper Germen Hukuk Bürosu' if tr else 'Alper Germen Law Office'}" />
<meta property="og:locale" content="{M["locale"]}" />
<meta property="og:title" content="{M["ad"]} | Av. Alper Germen" />
<meta property="og:description" content="{M["desc"]}" />
<meta property="og:url" content="{M["url"]}" />
<meta property="og:image" content="{SITE}/assets/avukat.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{M["ad"]} | Av. Alper Germen" />
<meta name="twitter:description" content="{M["desc"]}" />
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
    <div class="ph-no">{M["no"]}</div>
    <div class="crumbs"><a href="{'/' if tr else '/en/'}">{M["ana"]}</a> — <span>{M["kirilim"]}</span></div>
    <h1>{M["h1_a"]} <em>{M["h1_b"]}</em></h1>
    <p class="ph-lead">{M["lead"]}</p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <h2 class="h-section rv">{M["h2"]}</h2>
    <p class="rv d1" style="max-width:72ch;margin-top:16px;color:var(--cream-soft);font-size:15px;line-height:1.78">{M["giris"]}</p>
    <div class="art-grid makale-liste rv d2">{kartlar}
    </div>
  </div>
</section>

<section class="section tight lp-blok">
  <div class="wrap lp-wrap">
    <h2>{M["h2b"]}</h2>{nasil}
  </div>
</section>

{alt}
<script src="/{'main.js' if tr else 'main-en.js'}" defer></script>
</body>
</html>
"""


def uret():
    for tr, yol in ((True, "bulten"), (False, "en/legal-updates")):
        d = PUB / yol
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(sayfa(tr))
        print("yazildi:", yol + "/index.html")


if __name__ == "__main__":
    uret()
