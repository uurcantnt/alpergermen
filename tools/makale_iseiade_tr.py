# -*- coding: utf-8 -*-
"""İşe iade davası (4857 sayılı İş Kanunu m. 18-21). Bülten dışı, alan yazısı.

NOT: kacis() yalnızca <a> etiketlerini korur; başka HTML etiketi kullanılmaz.
"""

SLUG = "yazilar/ise-iade-davasi-sartlari-ve-sureleri"
TITLE = "İşe İade Davası: Şartları ve Süreleri | Av. Alper Germen"
DESC = ("İşe iade davasının şartları: otuz işçi ve altı ay kıdem, bir aylık arabuluculuk süresi, "
        "iki haftalık dava süresi, on iş günü başvuru ve dört ilâ sekiz aylık tazminat.")
H1 = "İşe İade Davası: Şartlar, Süreler ve Sonuçlar"
KICKER = "İş Hukuku"
ARTICLE_SECTION = "İş Hukuku"
TARIH = "2026-09-03T09:00:00+03:00"
RG_LINK = "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.4857.pdf"

OZET = ("İş güvencesi kapsamındaki bir işçinin sözleşmesi geçerli bir sebep gösterilmeden "
        "feshedildiğinde işe iade talep edebilir. Bu yazıda davanın kapsam şartları, arabuluculuk ve "
        "dava süreleri, ispat yükü ile kararın kesinleşmesinden sonra işleyen başvuru ve işe başlatma "
        "süreleri ele alınmaktadır.")

GIRIS = [
 ("İş güvencesi, işverenin fesih hakkını geçerli bir sebep gösterme yükümlülüğüne bağlayan bir "
  "kurumdur. 4857 sayılı İş Kanunu'nun 18 ilâ 21. maddeleri bu güvenceyi ve ihlali hâlinde işleyecek "
  "usulü düzenler."),
 ("Uygulamada dosyaların önemli bir kısmı esasa girilmeden, kapsam şartlarının veya sürelerin "
  "kaçırılmış olması nedeniyle sonuçlanır. Bu nedenle aşağıda önce kapsam, sonra süreler ele "
  "alınmaktadır. Büronun bu alandaki çalışmaları "
  "<a href=\"/antalya-is-hukuku-avukati/\">Antalya iş hukuku avukatı</a> sayfasında anlatılmıştır."),
 ("Yazıdaki süre ve tutarlar 4857 sayılı İş Kanunu ile 7036 sayılı İş Mahkemeleri Kanunu'nun "
  "yürürlükteki metnine dayanmaktadır."),
]

BOLUMLER = [
 ("Kim işe iade davası açabilir?", [
   "İş Kanunu'nun 18. maddesi, iş güvencesinden yararlanacak işçiyi üç ölçütle belirlemektedir.",
   "Birincisi işyeri ölçütüdür: işyerinde otuz veya daha fazla işçi çalıştırılıyor olmalıdır. Bu sayı "
   "işverenin aynı iş kolundaki tüm işyerlerinde çalışan işçi sayısı esas alınarak belirlenir.",
   "İkincisi kıdem ölçütüdür: işçinin en az altı aylık kıdemi bulunmalıdır. Altı aylık kıdem hesabında "
   "Kanunun 66. maddesindeki süreler dikkate alınır. Yer altı işlerinde çalışan işçilerde kıdem şartı "
   "aranmaz.",
   "Üçüncüsü sözleşme ölçütüdür: iş sözleşmesi belirsiz süreli olmalıdır. Belirli süreli bir "
   "sözleşmenin süresinin dolmasıyla sona ermesi hâlinde işe iade davası açılamaz.",
   "Bu üç şart birlikte gerçekleşmedikçe işe iade davası dinlenmez; bu durumda işçinin talepleri "
   "kötüniyet tazminatı ve ihbar tazminatı gibi başka başlıklar altında değerlendirilir."]),

 ("Geçerli sebep nedir, hangi hâller geçerli sayılmaz?", [
   "Belirsiz süreli iş sözleşmesini fesheden işveren; işçinin yeterliliğinden veya davranışlarından ya "
   "da işletmenin, işyerinin veya işin gereklerinden kaynaklanan geçerli bir sebebe dayanmak "
   "zorundadır.",
   "Kanun, geçerli sebep oluşturmayacak hâlleri ayrıca saymıştır. Sendika üyeliği veya çalışma saatleri "
   "dışında ya da işverenin rızasıyla çalışma saatleri içinde sendikal faaliyetlere katılmak geçerli "
   "sebep değildir.",
   "İşyeri sendika temsilciliği yapmak; mevzuattan veya sözleşmeden doğan hakları takip ya da "
   "yükümlülükleri yerine getirmek için işveren aleyhine idari veya adli makamlara başvurmak veya bu "
   "hususta başlatılmış sürece katılmak da geçerli sebep sayılmaz.",
   "Irk, renk, cinsiyet, medeni hâl, aile yükümlülükleri, hamilelik, doğum, din, siyasi görüş ve "
   "benzeri nedenler ile Kanunun 74. maddesinde öngörülen ve kadın işçilerin çalıştırılmasının yasak "
   "olduğu sürelerde işe gelmemek de bu listede yer alır."]),

 ("Feshin usulü: yazılı bildirim ve savunma", [
   "Kanunun 19. maddesi feshin şekline ilişkin iki zorunluluk getirmektedir.",
   "Birincisi yazılılıktır: işveren fesih bildirimini yazılı olarak yapmak ve fesih sebebini açık ve "
   "kesin bir şekilde belirtmek zorundadır. Sebebin sonradan değiştirilmesi ya da genişletilmesi kural "
   "olarak mümkün değildir.",
   "İkincisi savunmadır: hakkındaki iddialara karşı savunması alınmadan bir işçinin belirsiz süreli iş "
   "sözleşmesi, o işçinin davranışı veya verimi ile ilgili nedenlerle feshedilemez.",
   "Savunma alma yükümlülüğünün istisnası, işverenin 25. maddenin (II) numaralı bendi şartlarına uygun "
   "fesih hakkının saklı tutulmasıdır. Yani ahlak ve iyi niyet kurallarına uymayan hâllere dayanan "
   "haklı nedenle derhâl fesihte bu zorunluluk aranmaz."]),

 ("İlk süre: bir ay içinde arabulucuya başvuru", [
   "İşe iade sürecinin ilk adımı dava değil arabuluculuktur ve bu bir dava şartıdır.",
   "İş sözleşmesi feshedilen işçi; fesih bildiriminde sebep gösterilmediği veya gösterilen sebebin "
   "geçerli olmadığı iddiasıyla, fesih bildiriminin tebliği tarihinden itibaren bir ay içinde işe iade "
   "talebiyle arabulucuya başvurmak zorundadır.",
   "7036 sayılı İş Mahkemeleri Kanunu'nun 3. maddesi uyarınca işe iade talebiyle açılan davalarda "
   "arabulucuya başvurulmuş olması dava şartıdır. Arabulucuya başvurulmadan dava açıldığının "
   "anlaşılması hâlinde, herhangi bir işlem yapılmaksızın dava, dava şartı yokluğu sebebiyle usulden "
   "reddedilir.",
   "Sürenin başlangıcı fesih tarihi değil, fesih bildiriminin tebliğ tarihidir. Bildirimin ne zaman ve "
   "nasıl tebliğ edildiğinin belgelenmesi bu nedenle önem taşır."]),

 ("İkinci süre: iki hafta içinde dava", [
   "Arabuluculuk faaliyeti sonunda anlaşmaya varılamaması hâlinde, son tutanağın düzenlendiği tarihten "
   "itibaren iki hafta içinde iş mahkemesinde dava açılabilir.",
   "Taraflar anlaşırlarsa uyuşmazlık aynı sürede iş mahkemesi yerine özel hakeme de götürülebilir.",
   "Davacı, anlaşmaya varılamadığına ilişkin son tutanağın aslını veya arabulucu tarafından onaylanmış "
   "bir örneğini dava dilekçesine eklemek zorundadır. Eklenmemesi hâlinde mahkeme bir haftalık kesin "
   "süre verir; ihtarın gereği yerine getirilmezse dava dilekçesi karşı tarafa tebliğe çıkarılmaksızın "
   "dava usulden reddedilir.",
   "Arabulucuya başvurmaksızın doğrudan dava açılması sebebiyle davanın usulden reddi hâlinde ret "
   "kararı taraflara resen tebliğ edilir. Kesinleşen ret kararının resen tebliğinden itibaren iki hafta "
   "içinde arabulucuya başvurulabilir."]),

 ("İspat yükü kimde?", [
   "Kanunun 20. maddesi ispat yükünü açık biçimde dağıtmaktadır.",
   "Feshin geçerli bir sebebe dayandığını ispat yükümlülüğü işverene aittir. İşveren, dayandığı sebebi "
   "ve bu sebebin geçerliliğini ortaya koymak durumundadır.",
   "İşçi, feshin başka bir sebebe dayandığını iddia ettiği takdirde bu iddiasını ispatla yükümlüdür. "
   "Örneğin sendikal nedenle veya bir şikâyet başvurusu üzerine fesih yapıldığı ileri sürülüyorsa, bu "
   "iddianın ispatı işçiye düşer.",
   "Dava ivedilikle sonuçlandırılır. Mahkemece verilen karar hakkında istinaf yoluna başvurulması "
   "hâlinde, bölge adliye mahkemesi ivedilikle ve kesin olarak karar verir. Bu, işe iade davalarında "
   "temyiz yolunun kapalı olduğu anlamına gelir."]),

 ("Karar verildikten sonra işleyen süreler", [
   "Feshin geçersizliğine karar verilmesi tek başına işçiyi işe iade etmez; kanun iki ayrı süre daha "
   "öngörmüştür ve bu süreler uygulamada en çok hak kaybına yol açan noktadır.",
   "İşçi, kesinleşen mahkeme veya özel hakem kararının tebliğinden itibaren on iş günü içinde işe "
   "başlamak için işverene başvuruda bulunmak zorundadır. Bu süre iş günü olarak hesaplanır.",
   "İşveren ise işçiyi bir ay içinde işe başlatmak zorundadır. Başvuru üzerine işveren bir ay içinde "
   "işe başlatmazsa, işçiye en az dört aylık ve en çok sekiz aylık ücreti tutarında tazminat ödemekle "
   "yükümlü olur.",
   "Mahkeme veya özel hakem, feshin geçersizliğine karar verirken işçinin işe başlatılmaması hâlinde "
   "ödenecek tazminat miktarını da belirler. Bu tazminat, dava tarihindeki ücret esas alınarak parasal "
   "olarak belirlenir."]),

 ("Boşta geçen süre ücreti ve mahsup", [
   "Kararın kesinleşmesine kadar çalıştırılmadığı süre için işçiye en çok dört aya kadar doğmuş bulunan "
   "ücret ve diğer hakları ödenir. Bu kalem, işe başlatılsın veya başlatılmasın işçiye ödenir.",
   "Boşta geçen süre ücreti de, işe başlatmama tazminatı gibi, dava tarihindeki ücret esas alınarak "
   "parasal olarak belirlenir.",
   "İşçi işe başlatılırsa, peşin olarak ödenen bildirim süresine ait ücret ile kıdem tazminatı, "
   "yapılacak ödemeden mahsup edilir. Böylece aynı dönem için iki kez ödeme yapılması önlenir.",
   "İşe başlatılmayan işçiye bildirim süresi verilmemiş veya bildirim süresine ait ücret peşin "
   "ödenmemişse, bu sürelere ait ücret tutarı ayrıca ödenir."]),

 ("Dosya hazırlığında dikkat edilecek noktalar", [
   "İlk belge fesih bildirimidir. Bildirimin yazılı olup olmadığı, sebebin açık ve kesin biçimde "
   "gösterilip gösterilmediği ve tebliğ tarihi, hem esas hem süre bakımından belirleyicidir.",
   "İkinci belge savunma tutanağıdır. Davranış veya verim gerekçeli fesihlerde savunma alınmamış olması "
   "başlı başına geçersizlik sebebi olarak değerlendirilir.",
   "Üçüncü konu işçi sayısıdır. Otuz işçi ölçütü çekişmeli hâle geldiğinde SGK kayıtları ve işverenin "
   "aynı iş kolundaki diğer işyerleri incelenir; bu inceleme genellikle davanın ilk aşamasında yapılır.",
   "Dördüncü konu takvimdir. Bir aylık arabuluculuk ve iki haftalık dava süreleri hak düşürücü "
   "niteliktedir; kaçırıldığında esas incelenmeksizin sonuç doğar. Antalya ve Konyaaltı'ndaki "
   "dosyalarda izlenen genel yol için <a href=\"/konyaalti-avukat/\">Konyaaltı avukat</a> sayfası "
   "incelenebilir."]),
]

SSS = [
 ("İşe iade davası açmak için kaç işçi şartı var?",
  "İşyerinde otuz veya daha fazla işçi çalıştırılıyor olması gerekir. İşçi sayısı, işverenin aynı iş "
  "kolundaki tüm işyerlerinde çalışan işçi sayısı esas alınarak belirlenir."),
 ("Altı aylık kıdem nasıl hesaplanır?",
  "Altı aylık kıdem hesabında İş Kanunu'nun 66. maddesindeki süreler dikkate alınır. Yer altı "
  "işlerinde çalışan işçilerde kıdem şartı aranmaz."),
 ("İşe iade için önce arabulucuya mı gidilir?",
  "Evet. İşçi, fesih bildiriminin tebliği tarihinden itibaren bir ay içinde işe iade talebiyle "
  "arabulucuya başvurmak zorundadır; bu bir dava şartıdır."),
 ("Arabuluculukta anlaşma olmazsa dava süresi ne kadar?",
  "Anlaşmaya varılamaması hâlinde, son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş "
  "mahkemesinde dava açılabilir. Taraflar anlaşırsa aynı sürede özel hakeme de gidilebilir."),
 ("Feshin geçerli olduğunu kim ispat eder?",
  "Feshin geçerli bir sebebe dayandığını ispat yükümlülüğü işverene aittir. İşçi feshin başka bir "
  "sebebe dayandığını iddia ederse, bu iddiasını ispatla yükümlüdür."),
 ("Kararı kazanan işçi ne yapmalı?",
  "İşçi, kesinleşen kararın tebliğinden itibaren on iş günü içinde işe başlamak için işverene "
  "başvurmak zorundadır. İşveren başvuru üzerine bir ay içinde işe başlatmalıdır."),
 ("İşe başlatılmazsam ne alırım?",
  "İşveren bir ay içinde işe başlatmazsa en az dört, en çok sekiz aylık ücret tutarında tazminat "
  "ödenir. Ayrıca kararın kesinleşmesine kadar çalıştırılmayan süre için en çok dört aya kadar ücret "
  "ve diğer haklar ödenir."),
 ("İşe iade kararına karşı temyiz yolu var mı?",
  "Dava ivedilikle sonuçlandırılır ve istinaf başvurusu hâlinde bölge adliye mahkemesi ivedilikle ve "
  "kesin olarak karar verir."),
]

KAPANIS = [
 "İşe iade dosyalarında sonucu belirleyen iki unsur vardır: kapsam şartlarının baştan doğru "
 "değerlendirilmesi ve takvimin kaçırılmaması. Bir aylık arabuluculuk ve iki haftalık dava süreleri ile "
 "karar sonrası on iş günlük başvuru süresi, kaçırıldığında esasa girilmeksizin sonuç doğuran "
 "sürelerdir.",
 "Büronun çalışma alanları <a href=\"/alanlar\">çalışma alanları sayfasında</a> yer almaktadır. "
 "Dosyanıza özgü değerlendirme için <a href=\"/iletisim\">iletişim sayfası</a> üzerinden büroya "
 "ulaşabilirsiniz.",
]

UYARI = ("Bu yazı yalnızca genel bilgilendirme amacıyla hazırlanmıştır; hukuki görüş veya tavsiye "
         "niteliği taşımaz. İşe iade dosyalarında sonuç; işyerindeki işçi sayısına, kıdeme, fesih "
         "sebebine ve sürelere göre değişir. Somut bir dosya için avukata başvurulması gerekir.")
