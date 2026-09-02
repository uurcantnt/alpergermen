# -*- coding: utf-8 -*-
"""Saklı pay ve tenkis davası (TMK). Türkçe içerik — bülten dışı, alan yazısı.

NOT: kacis() yalnızca <a> etiketlerini korur; başka HTML etiketi kullanılmaz.
"""

SLUG = "yazilar/sakli-pay-ve-tenkis-davasi"
TITLE = "Saklı Pay ve Tenkis Davası | Av. Alper Germen"
DESC = ("Mirasta saklı pay oranları, tenkise tabi kazandırmalar, tenkis davasında bir yıllık ve "
        "on yıllık süreler ile def'i yoluyla ileri sürme imkânı.")
H1 = "Mirasta Saklı Pay ve Tenkis Davası"
KICKER = "Miras Hukuku"
ARTICLE_SECTION = "Miras Hukuku"
TARIH = "2026-09-02T09:00:00+03:00"
RG_LINK = "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.4721.pdf"

OZET = ("Mirasbırakan malvarlığı üzerinde dilediği gibi tasarruf edemez; kanun bazı mirasçılara "
        "dokunulamayan bir pay ayırmıştır. Bu paya saklı pay, saklı payı aşan tasarrufların "
        "indirilmesini sağlayan davaya ise tenkis davası denir. Bu yazıda saklı pay oranları, hangi "
        "kazandırmaların tenkise tabi olduğu ve davanın süreleri ele alınmaktadır.")

GIRIS = [
 ("Miras hukukunda mirasbırakanın tasarruf özgürlüğü sınırsız değildir. Türk Medenî Kanunu, belirli "
  "mirasçılar bakımından terekede dokunulamayacak bir oran öngörmüştür."),
 ("Uygulamada bu kural en çok iki durumda gündeme gelir: mirasbırakanın vasiyetname veya miras "
  "sözleşmesiyle malvarlığının büyük bölümünü belirli kişilere bırakması ve sağlığında yaptığı "
  "devirlerle terekeyi boşaltması. Büronun bu alandaki çalışmaları "
  "<a href=\"/antalya-miras-avukati/\">Antalya miras avukatı</a> sayfasında anlatılmıştır."),
 ("Aşağıda önce saklı pay kavramı ve oranları, ardından tenkis davasının koşulları, kapsamı ve "
  "süreleri ele alınmaktadır. Yazıdaki oran ve süreler Türk Medenî Kanunu'nun yürürlükteki "
  "metnine dayanmaktadır."),
]

BOLUMLER = [
 ("Saklı pay nedir?", [
   "Saklı pay, kanunun belirli mirasçılara ayırdığı ve mirasbırakanın ölüme bağlı tasarruflarla ya da "
   "sağlararası kazandırmalarla ortadan kaldıramayacağı asgari paydır.",
   "Terekenin saklı paylar dışında kalan kısmına tasarruf edilebilir kısım denir. Mirasbırakan bu "
   "kısım üzerinde serbestçe tasarruf edebilir; saklı payları aşan tasarruflar ise tenkise tabidir.",
   "Saklı pay, yasal miras payının kendisi değil, o payın kanunda gösterilen bir oranıdır. Bu nedenle "
   "hesap iki aşamalıdır: önce mirasçının yasal miras payı, sonra bu payın saklı pay oranı bulunur."]),

 ("Saklı pay oranları kimler için ne kadar?", [
   "Türk Medenî Kanunu'nun 506. maddesi saklı pay sahiplerini ve oranlarını saymaktadır.",
   "Altsoy için saklı pay, yasal miras payının yarısıdır. Altsoy; çocuklar, onlar hayatta değilse "
   "torunlar şeklinde devam eder.",
   "Ana ve babadan her biri için saklı pay, yasal miras payının dörtte biridir.",
   "Sağ kalan eş bakımından oran ikiye ayrılmıştır: altsoy veya ana ve baba zümresiyle birlikte "
   "mirasçı olması hâlinde yasal miras payının tamamı; diğer hâllerde yasal miras payının dörtte "
   "üçüdür.",
   "Kardeşlerin saklı payı 2007 yılında yapılan değişiklikle kaldırılmıştır. Bu nedenle kardeşler "
   "yasal mirasçı olsalar dahi saklı pay sahibi değildir ve tenkis davası açamazlar."]),

 ("Tenkis davası hangi hâllerde açılır?", [
   "Kanunun 560. maddesine göre saklı paylarının karşılığını alamayan mirasçılar, mirasbırakanın "
   "tasarruf edebileceği kısmı aşan tasarruflarının tenkisini dava edebilirler.",
   "Davanın amacı tasarrufu tümüyle geçersiz kılmak değildir; tasarrufu, tasarruf edilebilir kısma "
   "indirmektir. Bu yönüyle tenkis davası bir iptal davası değildir.",
   "Aynı maddede önemli bir yorum kuralı yer alır: yasal mirasçıların paylarına ilişkin olarak "
   "tasarrufta yer alan kurallar, mirasbırakanın arzusunun başka türlü olduğu tasarruftan "
   "anlaşılmadıkça sadece paylaştırma kuralı sayılır.",
   "Davacı, saklı payı zedelenen mirasçıdır. Davalı ise kazandırmadan yararlanan kişidir; bu bir "
   "mirasçı olabileceği gibi üçüncü kişi de olabilir."]),

 ("Sağlararası kazandırmalar da tenkise tabi mi?", [
   "Evet. Tenkis yalnızca vasiyetname gibi ölüme bağlı tasarrufları değil, mirasbırakanın sağlığında "
   "yaptığı bazı karşılıksız kazandırmaları da kapsar. Bunlar Kanunun 565. maddesinde dört bent "
   "hâlinde sayılmıştır.",
   "Birinci bent; mirasçılık sıfatını kaybeden yasal mirasçıya miras payına mahsuben yapılmış "
   "sağlararası kazandırmaları, geri verilmemek kaydıyla altsoya malvarlığı devri veya borçtan "
   "kurtarma yoluyla yapılan kazandırmaları ve alışılmışın dışında verilen çeyiz ile kuruluş "
   "sermayesini kapsar.",
   "İkinci bent, miras haklarının ölümden önce tasfiyesi maksadıyla yapılan kazandırmalara ilişkindir.",
   "Üçüncü bent, mirasbırakanın serbestçe dönme hakkını saklı tutarak yaptığı bağışlamalar ile "
   "ölümünden önceki bir yıl içinde âdet üzere verilen hediyeler dışında yaptığı bağışlamaları "
   "kapsar. Ölümden önceki bir yıl ölçütü uygulamada sık başvurulan bir sınırdır.",
   "Dördüncü bent ise en geniş olanıdır: mirasbırakanın saklı pay kurallarını etkisiz kılmak amacıyla "
   "yaptığı açık olan kazandırmalar. Muvazaalı satış görünümündeki devirler çoğu zaman bu bent "
   "kapsamında tartışılır."]),

 ("Tenkis nasıl hesaplanır?", [
   "Kanunun 507. maddesine göre tasarruf edilebilir kısım, terekenin mirasbırakanın ölümü günündeki "
   "durumuna göre hesaplanır. Hesap yapılırken mirasbırakanın borçları, cenaze giderleri, terekenin "
   "mühürlenmesi ve yazımı giderleri ile birlikte yaşayanların üç aylık geçim giderleri indirilir.",
   "Tenkis, mirasbırakanın arzusunun başka türlü olduğu tasarruftan anlaşılmadıkça, ölüme bağlı "
   "tasarrufla elde edilen kazandırmaların tamamında orantılı olarak yapılır.",
   "Bölünemeyen mal bakımından ayrı bir kural vardır. Değerinde azalma olmaksızın bölünmesine olanak "
   "bulunmayan belirli bir mal vasiyeti tenkise tabi olursa, vasiyet alacaklısı dilerse tenkisi "
   "gereken kısmın değerini ödeyerek malın verilmesini, dilerse tasarruf edilebilir kısmın değerini "
   "karşılayan parayı isteyebilir. Aynı kurallar sağlararası kazandırmaların tenkisinde de uygulanır.",
   "Bu nedenle taşınmaz devirlerine ilişkin tenkis dosyalarında bilirkişi incelemesi ve değer tespiti "
   "belirleyici olur."]),

 ("Süreler: bir yıl ve on yıl", [
   "Kanunun 571. maddesi tenkis davasının sürelerini düzenler ve bu süreler hak düşürücü niteliktedir.",
   "Tenkis davası açma hakkı, mirasçıların saklı paylarının zedelendiğini öğrendikleri tarihten "
   "başlayarak bir yıl geçmekle düşer.",
   "Her hâlde; vasiyetnamelerde açılma tarihinin, diğer tasarruflarda ise mirasın açılması tarihinin "
   "üzerinden on yıl geçmekle dava hakkı düşer.",
   "Bir tasarrufun iptali bir öncekinin yürürlüğe girmesini sağlarsa, süreler iptal kararının "
   "kesinleşmesi tarihinde işlemeye başlar.",
   "Maddenin son cümlesi uygulamada büyük önem taşır: tenkis iddiası, def'i yoluyla her zaman ileri "
   "sürülebilir. Yani dava açma süresi geçmiş olsa dahi, saklı payı zedelenen mirasçı kendisine karşı "
   "açılan bir davada tenkis iddiasını savunma olarak ileri sürebilir."]),

 ("Muris muvazaası ile tenkis arasındaki fark", [
   "Uygulamada en sık karışan iki yol budur. Muris muvazaası, mirasbırakanın mirasçılardan mal "
   "kaçırmak amacıyla gerçekte bağış olan bir devri satış gibi göstermesi hâlinde gündeme gelir ve "
   "tapu iptali ile tescil talebiyle yürütülür.",
   "Tenkis davasında ise devrin görünürdeki niteliği tartışılmaz; kazandırmanın saklı payı "
   "zedelediği ileri sürülerek tasarruf edilebilir kısma indirilmesi istenir.",
   "İki yolun sonucu da farklıdır. Muvazaa iddiası kabul edilirse devir baştan geçersiz sayılır ve "
   "taşınmaz terekeye döner; tenkiste ise kazandırma ayakta kalır, yalnızca saklı payı aşan kısım "
   "indirilir.",
   "Süre bakımından da ayrılırlar: tenkis davası bir yıllık ve on yıllık hak düşürücü sürelere tabi "
   "iken, muvazaa iddiası bakımından bu süreler uygulanmaz.",
   "Hangi yolun izleneceği, devrin biçimine ve elde bulunan delillere göre belirlenir; iki talep "
   "birlikte de ileri sürülebilir."]),

 ("Görevli ve yetkili mahkeme", [
   "Tenkis davalarında görevli mahkeme asliye hukuk mahkemesidir.",
   "Yetki bakımından kural, mirasbırakanın son yerleşim yeri mahkemesidir. Bu kural miras "
   "davalarında kesin yetki niteliği taşıdığından, tarafların anlaşmasıyla değiştirilemez.",
   "Antalya'da mirasbırakanın son yerleşim yeri Antalya ise dava Antalya Adalet Sarayı'ndaki asliye "
   "hukuk mahkemelerinde görülür; Konyaaltı, Muratpaşa ve Kepez ilçelerinin ayrı adliyesi "
   "bulunmamaktadır.",
   "Dava açılmadan önce tereke tespiti, tapu kayıtlarının ve devir tarihlerinin çıkarılması ile veraset "
   "ilamının temin edilmesi, hem süre hesabı hem de dava değeri bakımından ilk adımdır."]),
]

SSS = [
 ("Saklı pay oranları nedir?",
  "Altsoy için yasal miras payının yarısı, ana ve babadan her biri için yasal miras payının dörtte "
  "biri; sağ kalan eş için altsoy veya ana-baba zümresiyle birlikte mirasçı olması hâlinde yasal miras "
  "payının tamamı, diğer hâllerde dörtte üçüdür."),
 ("Kardeşler tenkis davası açabilir mi?",
  "Hayır. Kardeşlerin saklı payı 2007 yılında yapılan değişiklikle kaldırılmıştır. Kardeşler yasal "
  "mirasçı olsalar dahi saklı pay sahibi olmadıkları için tenkis davası açamazlar."),
 ("Mirasbırakanın sağlığında yaptığı bağışlar tenkise tabi mi?",
  "Kanunun 565. maddesinde sayılan karşılıksız kazandırmalar ölüme bağlı tasarruflar gibi tenkise "
  "tabidir. Bunlar arasında serbestçe dönme hakkı saklı tutularak yapılan bağışlamalar, ölümden "
  "önceki bir yıl içinde âdet üzere verilen hediyeler dışındaki bağışlamalar ve saklı pay kurallarını "
  "etkisiz kılmak amacıyla yapıldığı açık olan kazandırmalar yer alır."),
 ("Tenkis davası ne kadar sürede açılmalı?",
  "Saklı payın zedelendiğinin öğrenildiği tarihten başlayarak bir yıl, her hâlde vasiyetnamelerde "
  "açılma tarihinden, diğer tasarruflarda mirasın açılması tarihinden itibaren on yıl içinde açılmalıdır. "
  "Bu süreler hak düşürücüdür."),
 ("Süre geçtiyse hiçbir şey yapılamaz mı?",
  "Tenkis iddiası def'i yoluyla her zaman ileri sürülebilir. Dava açma süresi geçmiş olsa dahi, saklı "
  "payı zedelenen mirasçı kendisine karşı açılan bir davada tenkis iddiasını savunma olarak ileri "
  "sürebilir."),
 ("Tenkis davası ile muris muvazaası aynı şey mi?",
  "Değildir. Muris muvazaasında gerçekte bağış olan bir devrin satış gibi gösterildiği ileri sürülür "
  "ve tapu iptali ile tescil istenir. Tenkiste ise kazandırma ayakta kalır, yalnızca saklı payı aşan "
  "kısım tasarruf edilebilir orana indirilir."),
 ("Tenkis davası hangi mahkemede açılır?",
  "Görevli mahkeme asliye hukuk mahkemesidir. Yetkili mahkeme ise mirasbırakanın son yerleşim yeri "
  "mahkemesidir ve bu yetki kesindir."),
]

KAPANIS = [
 "Tenkis dosyalarında sonucu belirleyen üç unsur; saklı pay sahiplerinin ve oranlarının doğru "
 "belirlenmesi, tenkise tabi kazandırmaların eksiksiz tespiti ve sürelerin kaçırılmamasıdır. "
 "Özellikle sağlararası devirlerin tarih ve biçim yönünden incelenmesi çoğu zaman davanın seyrini "
 "değiştirir.",
 "Büronun çalışma alanları <a href=\"/alanlar\">çalışma alanları sayfasında</a> yer almaktadır. "
 "Dosyanıza özgü değerlendirme için <a href=\"/iletisim\">iletişim sayfası</a> üzerinden büroya "
 "ulaşabilirsiniz.",
]

UYARI = ("Bu yazı yalnızca genel bilgilendirme amacıyla hazırlanmıştır; hukuki görüş veya tavsiye "
         "niteliği taşımaz. Tenkis dosyalarında sonuç; mirasçılık sıfatına, terekenin yapısına, "
         "devirlerin tarih ve biçimine göre değişir. Somut bir dosya için avukata başvurulması gerekir.")
