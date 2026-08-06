# Google Yorumları — Nasıl Güncellenir

Anasayfadaki **Değerlendirmeler** bölümü elle güncellenir. Google Places API'ye
bağlı **değildir**: API'nin yorum döndüren katmanı ücretlidir (ayda yalnızca
1.000 çağrı ücretsiz) ve en fazla 5 yorum verir. Elle liste tutmak hem ücretsizdir
hem de kaç yorum gösterileceğine siz karar verirsiniz.

Dosyalar:

| Dosya | İçerik |
|-------|--------|
| `public/main.js` | Türkçe sayfanın `REVIEWS` listesi |
| `public/main-en.js` | İngilizce sayfanın listesi (aynı yorumlar) |
| `public/index.html`, `public/en/index.html` | Bölüm ve alttaki Google butonu |
| `public/styles.css` | `.rev-*` stilleri |

## Yeni yorum eklemek

`public/main.js` dosyasında `const REVIEWS=[` satırını bulun ve listeye bir
satır ekleyin:

```js
{yildiz:5,kisi:'Ahmet K.',ne_zaman:'3 hafta önce',
 metin:"Buraya yorumun tam metni gelir."},
```

Alanlar:

- **yildiz** — 1–5 arası sayı
- **kisi** — Google'da göründüğü adı. Bilinmiyorsa `''` bırakın; kart isimsiz
  görünür, boşluk oluşmaz.
- **ne_zaman** — Google'daki ifadenin aynısı (`2 hafta önce`, `bir yıl önce`)
- **metin** — yorumun tam hâli. **Çift tırnak** kullanın; Türkçe kesme işareti
  (`Antalya'da`) tek tırnakla çakışır.

Aynı satırı `public/main-en.js` dosyasına da ekleyin. **Yorum metinlerini
çevirmeyin** — bir yorumu çevirmek onu değiştirmek olur; İngilizce sayfada da
orijinal dilinde kalır.

Sonra commit + push edin; Cloudflare kendiliğinden dağıtır (~30 saniye).

## Üstteki puan özeti

```js
const REVIEW_SUMMARY={rating:5.0,total:9};
```

- **rating** — Google'daki genel puan
- **total** — profildeki **toplam değerlendirme** sayısı (yalnızca yıldız
  verenler dâhil). Listedeki yorum sayısından fazla olabilir; nitekim şu an
  9 değerlendirmenin 6'sı yazılıdır, kalan 3'ü yalnızca yıldızdır ve kart
  üretmez.

## Sıralama

Liste hangi sırada yazılırsa o sırada görünür. Şu an **uzun yorumlar başta**
duruyor: ilk satır en dolu yorum, son satır en kısası.

## Izgara düzeni

Kart sayısına göre kendiliğinden ayarlanır (`public/styles.css`, `.rev-grid`):

| Yorum | Masaüstü |
|-------|----------|
| 1 | tek geniş kart |
| 2, 4 | 2 sütun |
| 3, 6, 9 | 3 sütun |
| 5 | üstte 3, altta 2 |

Tablette 2 sütuna, mobilde tek sütuna iner.

## Yorum silmek

İlgili satırı iki dosyadan da silin. Liste tamamen boşalırsa bölüm
kendiliğinden gizlenir (`if(!sec||!REVIEWS.length)return;`), sayfa bozulmaz.

---

## Notlar

- **Yıldızlar Google aramada çıkmaz.** İşletmenin kendi sitesinde kendi
  hakkındaki yorumları işaretlemesi Google'ın "self-serving reviews"
  politikasına girer; `LegalService` gibi Organization türlerinde yıldızlı
  sonuç verilmez. Bu yüzden sayfaya bilerek `aggregateRating` işaretlemesi
  eklenmemiştir.
- Alttaki buton ve başlıktaki bağlantı işletmenin Google kaydına gider:
  `https://www.google.com/maps?cid=7733764520542568322`
- Canlı API'ye dönmek isterseniz eski kod git geçmişinde durur:
  `git show 3ffa8d2:worker.js` (uç nokta, önbellek ve teşhis mantığıyla birlikte).
