# -*- coding: utf-8 -*-
"""CMK 231 — HAGB'nin yeniden yazılması (7589 sayılı Kanun). Türkçe içerik.

NOT: uret_makale.py'deki kacis() yalnızca <a> etiketlerini korur; başka HTML
etiketi kullanılmaz (bkz. 2026-08-30 düzeltmesi).
"""

SLUG = "yazilar/hagb-yeni-duzenleme-ve-istinaf-yolu"
TITLE = "HAGB: Yeni Düzenleme ve İstinaf Yolu | Av. Alper Germen"
DESC = ("7589 sayılı Kanunla CMK 231 yeniden yazıldı: HAGB kararına karşı istinaf yolu, "
        "denetim süresi ihlalinde yeni hüküm kurma imkânı ve uygulanmayacak suçlar.")
H1 = "HAGB: 7589 Sayılı Kanunla Gelen Yeni Düzenleme"
KICKER = "Ceza Hukuku"
ARTICLE_SECTION = "Ceza Hukuku"
TARIH = "2026-08-31T09:00:00+03:00"
GORSEL = "/assets/makale-hagb.jpg"
RG_LINK = "https://www.resmigazete.gov.tr/eskiler/2026/07/20260731.htm"

OZET = ("Hükmün açıklanmasının geri bırakılmasını düzenleyen Ceza Muhakemesi Kanunu'nun 231. "
        "maddesinin beşinci ilâ on dördüncü fıkraları, 31 Temmuz 2026'da yürürlüğe giren 7589 "
        "sayılı Kanunla yeniden yazıldı. İki yıllık sınır ve beş yıllık denetim süresi korunurken, "
        "karara karşı istinaf yolu, denetim süresi ihlalinde mahkemeye yeni bir hüküm kurma imkânı "
        "ve maddenin hiç uygulanmayacağı suçlar açıkça düzenlendi.")

GIRIS = [
 ("Düzenleme, kamuoyunda 12. Yargı Paketi olarak anılan 7589 sayılı Yargının Etkin ve Verimli "
  "İşlemesine Yönelik Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanunun 15. maddesiyle geldi. "
  "Kanun 31 Temmuz 2026 tarihli, 33326 sayılı Resmî Gazete'de yayımlanarak aynı gün yürürlüğe girdi."),
 ("Değişiklik maddenin tamamını değil, beşinci ilâ on dördüncü fıkralarını kapsıyor. Yani hükmün "
  "açıklanmasının geri bırakılmasının temel yapısı korunmuş, ancak kurumun işleyişine ilişkin "
  "hemen her kural yeniden kaleme alınmıştır. Büronun ceza hukuku alanındaki çalışmaları "
  "<a href=\"/antalya-ceza-avukati/\">Antalya ceza avukatı</a> sayfasında anlatılmıştır."),
 ("Aşağıda önce HAGB'nin ne olduğu ve hangi şartlarda verilebileceği, ardından yeni metnin getirdiği "
  "başlıklar ele alınmaktadır: kanun yolu, denetim süresi ihlalinin sonuçları ve maddenin "
  "uygulanmayacağı suçlar."),
]

BOLUMLER = [
 ("HAGB nedir, hangi cezalarda verilebilir?", [
   "Hükmün açıklanmasının geri bırakılması, mahkemenin sanık hakkında bir hüküm kurmasına rağmen bu "
   "hükmü açıklamamasıdır. Yürürlükteki metne göre HAGB, müsadereye ilişkin hükümler hariç olmak "
   "üzere, kurulan hükmün sanık hakkında bir hukuki sonuç doğurmamasını ifade eder.",
   "Uygulanabilmesi için hükmolunan cezanın iki yıl veya daha az süreli hapis ya da adli para cezası "
   "olması gerekir. Bu sınır değişmemiştir. Uzlaşmaya ilişkin hükümler saklıdır.",
   "Karar bir beraat değildir; ortada kurulmuş ama açıklanmamış bir mahkûmiyet hükmü vardır. Denetim "
   "süresi sorunsuz geçerse hüküm ortadan kaldırılır ve davanın düşmesine karar verilir."]),

 ("Verilme şartları: üç koşul", [
   "Maddenin altıncı fıkrası üç koşul saymaktadır ve bunların birlikte gerçekleşmesi aranır.",
   "Birincisi, sanığın daha önce kasıtlı bir suçtan mahkûm olmamış bulunmasıdır. Taksirli suçlardan "
   "mahkûmiyet bu koşulu engellemez.",
   "İkincisi, mahkemenin sanığın kişilik özellikleri ile duruşmadaki tutum ve davranışlarını göz "
   "önünde bulundurarak yeniden suç işlemeyeceği hususunda kanaate varmasıdır. Bu, kararın "
   "gerekçelendirilmesi gereken takdirî unsurudur.",
   "Üçüncüsü, suçun işlenmesiyle mağdurun veya kamunun uğradığı zararın aynen iade, suçtan önceki "
   "hâle getirme veya tazmin suretiyle tamamen giderilmesidir.",
   "Dokuzuncu fıkra bu üçüncü koşula bir esneklik getirmektedir: zararı derhal gideremeyen sanık "
   "hakkında, zararı denetim süresince aylık taksitler hâlinde ödemek suretiyle tamamen gidermesi "
   "koşuluyla da HAGB kararı verilebilir."]),

 ("Denetim süresi beş yıl, yükümlülükler en çok bir yıl", [
   "HAGB kararı verildiğinde sanık beş yıl süreyle denetim süresine tabi tutulur. Bu süre içinde "
   "kişi hakkında kasıtlı bir suç nedeniyle bir daha HAGB kararı verilemez.",
   "Mahkeme, denetim süresi içinde bir yılı geçmemek üzere belirleyeceği bir süreyle sanığa "
   "denetimli serbestlik tedbiri olarak yükümlülük getirebilir. Maddede sayılan yükümlülükler "
   "şunlardır: meslek veya sanat sahibi değilse bir eğitim programına devam etmesi; meslek veya "
   "sanat sahibiyse bir kamu kurumunda ya da aynı işi yapan bir başkasının gözetiminde ücret "
   "karşılığında çalıştırılması; belli yerlere gitmekten yasaklanması, belli yerlere devam etmekle "
   "yükümlü kılınması ya da takdir edilecek başka bir yükümlülüğü yerine getirmesi.",
   "Önemli bir usul kuralı da bu fıkrada yer alır: denetim süresi içinde dava zamanaşımı durur.",
   "Ayrıca yedinci fıkra uyarınca, açıklanması geri bırakılan hükümdeki hapis cezası ertelenemez ve "
   "kısa süreli olması hâlinde seçenek yaptırımlara çevrilemez."]),

 ("Denetim süresi ihlal edilirse ne olur?", [
   "Onuncu fıkra olumlu senaryoyu düzenler: denetim süresi içinde kasten yeni bir suç işlenmez ve "
   "denetimli serbestlik yükümlülüklerine uygun davranılırsa, açıklanması geri bırakılan hüküm "
   "ortadan kaldırılarak davanın düşmesine karar verilir.",
   "On birinci fıkra ise ihlal hâlini düzenler ve yeni metnin en belirgin yeniliklerinden birini "
   "içerir. Denetim süresi içinde kasten yeni bir suç işlenmesi veya yükümlülüklere aykırı "
   "davranılması hâlinde mahkeme hükmü açıklar.",
   "Ancak mahkeme burada mekanik biçimde eski hükmü açıklamakla sınırlı değildir. Yükümlülükleri "
   "yerine getiremeyen sanığın durumunu değerlendirerek cezanın yarısına kadar belirleyeceği bir "
   "kısmının infaz edilmemesine, ya da koşulları varsa hükümdeki hapis cezasının ertelenmesine veya "
   "seçenek yaptırımlara çevrilmesine karar vererek yeni bir mahkûmiyet hükmü kurabilir.",
   "Açıklanan veya yeni kurulan hükme karşı itiraz edilebilir. Maddede itiraz merciinin inceleme "
   "sınırı da çizilmiştir: itiraz mercii ancak bu fıkradaki koşullarla sınırlı olarak bir "
   "değerlendirme yapabilir."]),

 ("Kanun yolu: HAGB kararına karşı istinaf", [
   "On ikinci fıkra kanun yolunu düzenler. Bu fıkra 2024 yılında bir kez değiştirilmiş, 7589 sayılı "
   "Kanunla yeniden yazılmıştır; bu nedenle güncel metnin esas alınması gerekir.",
   "Yürürlükteki kurala göre, Ceza Muhakemesi Kanunu'nun 272. maddesinin üçüncü fıkrası hükümleri "
   "saklı kalmak üzere, hükmün açıklanmasının geri bırakılması kararına karşı istinaf yoluna "
   "başvurulabilir. Bölge adliye mahkemesi tarafından verilen kararlar hakkında 286. madde hükümleri "
   "uygulanır.",
   "HAGB kararının ilk derece mahkemesi sıfatıyla bölge adliye mahkemesi veya Yargıtay tarafından "
   "verilmesi hâlinde ise temyiz yoluna gidilebilir; burada da 272. maddenin üçüncü fıkrası saklıdır.",
   "İnceleme kapsamı da açıkça belirlenmiştir: istinaf ve temyiz yolunda karar ve hüküm, usul ve "
   "esasa ilişkin hukuka aykırılıklar yönünden incelenir. Bu ifade, denetimin yalnızca HAGB "
   "koşullarının varlığıyla sınırlı kalmadığını göstermektedir."]),

 ("Kayıt sistemi ve uygulanmayacak suçlar", [
   "On üçüncü fıkra uyarınca HAGB kararları bunlara mahsus bir sisteme kaydedilir. Bu kayıtlar, "
   "ancak bir soruşturma veya kovuşturmayla bağlantılı olarak Cumhuriyet savcısı, hâkim veya mahkeme "
   "tarafından istenmesi hâlinde ve maddede belirtilen amaç için kullanılabilir.",
   "On dördüncü fıkra ise maddenin uygulanmayacağı suçları saymaktadır. Hükmün açıklanmasının geri "
   "bırakılmasına ilişkin hükümler; işkence ve eziyet suçları ile kamu görevlisinin görevi sebebiyle "
   "işlediği ve Anayasanın 17. maddesi kapsamında kötü muamele kabul edilebilecek suçlar hakkında "
   "uygulanmaz.",
   "Bu istisna, kurumun kapsamını daraltan en somut hükümdür ve ilgili dosyalarda HAGB talebinin "
   "baştan değerlendirilmesini gerektirir."]),

 ("Değişiklik derdest dosyalara uygulanır mı?", [
   "7589 sayılı Kanun, birçok değişiklik için ayrıntılı geçiş hükümleri öngörmüştür. Buna karşılık "
   "Ceza Muhakemesi Kanunu'nun 231. maddesinde yapılan değişiklik için ayrı bir geçiş hükmü "
   "getirilmemiştir.",
   "Bu nedenle sorun, ceza muhakemesi hukukunun genel ilkeleri çerçevesinde çözülecektir. Muhakeme "
   "hukukuna ilişkin kurallar bakımından uygulama, maddi ceza hukukundaki lehe kanun ilkesinden "
   "farklı bir mantıkla yürür; buna karşılık kurulan hükmün ve cezanın sonuçlarını doğrudan "
   "etkileyen hükümler bakımından değerlendirme dosyanın somut durumuna göre yapılır.",
   "Pratik sonuç şudur: hâlen görülmekte olan bir dosyada hangi metnin uygulanacağı, kararın hangi "
   "tarihte verildiğine ve dosyanın hangi aşamada bulunduğuna göre belirlenecektir. Bu değerlendirme "
   "dosyaya özgüdür ve genel bir cevabı yoktur."]),

 ("Savunma bakımından öne çıkan başlıklar", [
   "Yeni metin, HAGB talebini üç ayrı aşamada gündeme getirmektedir ve her aşamanın kendi savunma "
   "stratejisi vardır.",
   "Karar aşamasında ağırlık, altıncı fıkradaki üç koşuldur. Özellikle zararın giderilmesi koşulu "
   "bakımından, derhal ödeme mümkün değilse dokuzuncu fıkradaki taksitli ödeme imkânının açıkça "
   "talep edilmesi gerekir.",
   "İhlal aşamasında ağırlık, on birinci fıkradaki takdir yetkisine kaymaktadır. Mahkemenin cezanın "
   "yarısına kadar bir kısmını infaz etmeme ya da erteleme veya seçenek yaptırıma çevirme imkânı "
   "bulunduğundan, yükümlülüğün neden yerine getirilemediğine ilişkin somut açıklama ve belgeler "
   "belirleyici olabilir.",
   "Kanun yolu aşamasında ise inceleme, usul ve esasa ilişkin hukuka aykırılıklar yönünden yapılır. "
   "Antalya'da görülen dosyalarda istinaf incelemesi Antalya Bölge Adliye Mahkemesi ceza daireleri "
   "tarafından yürütülür.",
   "Soruşturma ve kovuşturma aşamasındaki haklar için <a href=\"/antalya-ceza-avukati/\">Antalya ceza "
   "avukatı</a> sayfası incelenebilir."]),
]

SSS = [
 ("HAGB hangi cezalarda verilebilir?",
  "Yargılama sonunda hükmolunan cezanın iki yıl veya daha az süreli hapis ya da adli para cezası "
  "olması gerekir. Bu sınır 7589 sayılı Kanunla değiştirilmemiştir."),
 ("HAGB kararına karşı hangi kanun yoluna başvurulur?",
  "Yürürlükteki metne göre, Ceza Muhakemesi Kanunu'nun 272. maddesinin üçüncü fıkrası saklı kalmak "
  "üzere HAGB kararına karşı istinaf yoluna başvurulabilir. Karar ilk derece mahkemesi sıfatıyla "
  "bölge adliye mahkemesi veya Yargıtay tarafından verilmişse temyiz yoluna gidilebilir."),
 ("Denetim süresi ne kadar?",
  "Denetim süresi beş yıldır. Bu süre içinde kişi hakkında kasıtlı bir suç nedeniyle bir daha HAGB "
  "kararı verilemez. Mahkeme ayrıca bir yılı geçmemek üzere denetimli serbestlik yükümlülüğü "
  "belirleyebilir. Denetim süresi içinde dava zamanaşımı durur."),
 ("Denetim süresinde yeni suç işlenirse ne olur?",
  "Mahkeme hükmü açıklar. Ancak yükümlülükleri yerine getiremeyen sanığın durumunu değerlendirerek "
  "cezanın yarısına kadar bir kısmının infaz edilmemesine, koşulları varsa hapis cezasının "
  "ertelenmesine veya seçenek yaptırımlara çevrilmesine karar vererek yeni bir mahkûmiyet hükmü "
  "kurabilir. Bu hükme karşı itiraz edilebilir."),
 ("Zarar giderilemezse HAGB verilemez mi?",
  "Zararın derhal giderilememesi tek başına engel değildir. Sanık hakkında, zararı denetim süresince "
  "aylık taksitler hâlinde ödemek suretiyle tamamen gidermesi koşuluyla da HAGB kararı verilebilir."),
 ("HAGB hangi suçlarda uygulanmaz?",
  "Maddenin on dördüncü fıkrası uyarınca, işkence ve eziyet suçları ile kamu görevlisinin görevi "
  "sebebiyle işlediği ve Anayasanın 17. maddesi kapsamında kötü muamele kabul edilebilecek suçlar "
  "hakkında HAGB hükümleri uygulanmaz."),
 ("HAGB kararı adli sicilde görünür mü?",
  "HAGB kararları bunlara mahsus ayrı bir sisteme kaydedilir. Bu kayıtlar ancak bir soruşturma veya "
  "kovuşturmayla bağlantılı olarak Cumhuriyet savcısı, hâkim veya mahkeme tarafından istenmesi "
  "hâlinde ve maddede belirtilen amaçla kullanılabilir."),
]

KAPANIS = [
 "Yeni metin, HAGB'yi tek bir karar anına sıkışmış bir kurum olmaktan çıkarıp kanun yolu ve ihlal "
 "aşamalarıyla birlikte kurgulanmış bir bütün hâline getirmektedir. Bu nedenle karar aşamasında "
 "yapılan tercih, denetim süresi boyunca doğuracağı sonuçlarla birlikte değerlendirilmelidir.",
 "Büronun çalışma alanları <a href=\"/alanlar\">çalışma alanları sayfasında</a> yer almaktadır. "
 "Dosyanıza özgü değerlendirme için <a href=\"/iletisim\">iletişim sayfası</a> üzerinden büroya "
 "ulaşabilirsiniz.",
]

UYARI = ("Bu yazı yalnızca genel bilgilendirme amacıyla hazırlanmıştır; hukuki görüş veya tavsiye "
         "niteliği taşımaz. Hükmün açıklanmasının geri bırakılmasına ilişkin değerlendirme, suçun "
         "niteliğine, sanığın sicil durumuna ve dosyanın bulunduğu aşamaya göre değişir. Somut bir "
         "dosya için avukata başvurulması gerekir.")
