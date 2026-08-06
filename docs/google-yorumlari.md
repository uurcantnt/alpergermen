# Google Yorumları — Kurulum

Anasayfadaki **Değerlendirmeler** bölümü, Google Places API'den canlı olarak beslenir.
Kod hazırdır; bölüm yalnızca API'den yorum geldiğinde görünür, gelmezse kendini gizler.

İşleyiş:

- `worker.js` → `/api/reviews` uç noktası Google'ı çağırır ve sonucu önbelleğe alır
- `public/main.js` / `public/main-en.js` → bu uç noktayı çağırıp kartları basar
- `public/index.html` / `public/en/index.html` → `#reviews` bölümü (`hidden`)

Çalışması için iki gizli değer gerekir: `GOOGLE_PLACES_API_KEY` ve `GOOGLE_PLACE_ID`.

---

## 1. Google Cloud'da Places API'yi açın

1. https://console.cloud.google.com adresine girin
2. Üstten yeni bir proje oluşturun (ör. `alpergermen-site`)
3. **Faturalandırma** hesabı bağlayın — Places API kart bağlamadan çalışmaz
   (aşağıdaki kota adımı sayesinde ücret çıkması beklenmez)
4. **APIs & Services → Library** → `Places API (New)` arayın → **Enable**

> Dikkat: Eski "Places API" değil, **Places API (New)** olmalı. Kod yeni sürümün
> `places.googleapis.com/v1` uç noktasını kullanır.

## 2. API anahtarı oluşturun ve kısıtlayın

1. **APIs & Services → Credentials → Create credentials → API key**
2. Oluşan anahtarda **Edit API key**:
   - **Application restrictions: None**
     (çağrı tarayıcıdan değil Cloudflare sunucusundan gider; IP'ler sabit
     olmadığı için IP/referrer kısıtı burada çalışmaz)
   - **API restrictions: Restrict key** → yalnızca **Places API (New)** seçin
3. Anahtarı kopyalayın — birazdan Cloudflare'e gireceğiz

**Anahtar gizlidir.** Repoya, HTML'e veya JS dosyasına yazılmaz; yalnızca
Cloudflare secret olarak durur ve tarayıcıya hiç ulaşmaz.

## 3. Fatura sürprizini kotayla kapatın

Yorum içeren istekler Google'ın en pahalı katmanına girer
(*Place Details Enterprise + Atmosphere*) ve ayda yalnızca **1.000 çağrı ücretsizdir**.
Önbellek sayesinde normalde ayda ~60–250 çağrı yapılır, ama tavanı yine de sabitleyin:

1. **APIs & Services → Places API (New) → Quotas & System Limits**
2. Günlük istek limitini **50** yapın

Böylece bir hata durumunda bile ücretsiz kotanın dışına çıkılamaz.

## 4. Place ID'yi bulun

1. https://developers.google.com/maps/documentation/places/web-service/place-id
   sayfasındaki **Place ID Finder** aracını açın
2. Haritada `Av. Alper Germen Hukuk Bürosu` işletmesini aratın
3. Çıkan `ChIJ...` ile başlayan kimliği kopyalayın

İşletmenin Google Haritalar kaydı:
https://www.google.com/maps?cid=7733764520542568322

## 5. Cloudflare'e gizli değerleri girin

Cloudflare Dashboard → **Workers & Pages → alpergermen → Settings → Variables and Secrets**

**Add** ile iki kayıt ekleyin, tipini **Secret** seçin:

| İsim | Değer |
|------|-------|
| `GOOGLE_PLACES_API_KEY` | 2. adımdaki anahtar |
| `GOOGLE_PLACE_ID` | 4. adımdaki `ChIJ...` kimliği |

Kaydettikten sonra Worker kendini yeniden dağıtır.

## 6. Önbelleği KV'ye alın (önerilir)

`REVIEWS_KV` bağlanmazsa kod Cloudflare Cache API'ye düşer. O önbellek **her
Cloudflare lokasyonunda ayrıdır** — aynı içerik için Google'a lokasyon sayısı
kadar çağrı gider ve ücretsiz kota beklenmedik şekilde tükenebilir. KV ise
küreseldir, tek çağrı tüm dünyaya yeter.

1. Dashboard → **Storage & Databases → KV → Create instance**, isim: `alpergermen-reviews`
2. Oluşan **Namespace ID**'yi kopyalayın
3. `wrangler.jsonc` dosyasına ekleyin:

```jsonc
"kv_namespaces": [
  { "binding": "REVIEWS_KV", "id": "BURAYA_NAMESPACE_ID" }
]
```

4. Commit + push edin

## 7. Doğrulayın

```bash
curl "https://alpergermen.av.tr/api/reviews?lang=tr"
```

Yorumlar geldiyse `reviews` dizisi dolu döner ve anasayfada bölüm görünür.

Sorun varsa yanıttaki `error` alanı sebebi söyler:

| `error` | Anlamı | Çözüm |
|---------|--------|-------|
| `missing_config` | Secret'lar girilmemiş | 5. adım |
| `http_403` | Anahtar reddedildi | API kısıtlaması yanlış (2. adım) ya da Places API (New) açık değil (1. adım) |
| `http_404` | Place ID bulunamadı | 4. adımı tekrarlayın |
| `http_429` | Kota doldu | 3. adımdaki günlük limiti kontrol edin |
| `no_reviews` | API çalışıyor, profilde yorum yok | Google profiline yorum gelmesini bekleyin |
| `fetch_failed` | Google'a ulaşılamadı | Geçicidir, 10 dk sonra kendini dener |

Önbellek süreleri duruma göre değişir:

| Durum | Süre | Neden |
|-------|------|-------|
| Yorum geldi | 24 saat | Yorumlar sık değişmez |
| `no_reviews` | 6 saat | Bu da faturalanan başarılı bir çağrıdır; sık tekrarlanırsa kota tükenir |
| Yapılandırma hatası | 10 dakika | Hatalı istekler faturalanmaz, düzeltmesi hızlı yansımalı |

Yani yeni bir yorum sitede en geç ertesi gün görünür; secret düzeltmesi ise
en geç 10 dakikada etkisini gösterir.

Kendi tarayıcınızda hemen görmek isterseniz sert yenileme yapın
(<kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>) ya da gizli sekme açın —
yanıtı daha önce almış bir tarayıcı süresi dolana kadar kendi kopyasını gösterir.

Kendi tarayıcınızda hemen görmek isterseniz sert yenileme yapın
(<kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>) ya da gizli sekme açın —
yanıtı daha önce almış bir tarayıcı süresi dolana kadar kendi kopyasını gösterir.

---

## Bilinen sınırlar

- **Google en fazla 5 yorum döndürür** ve hangilerinin döneceğini kendisi seçer;
  seçme veya sıralama imkânı yoktur.
- **Yıldızlar Google aramada çıkmaz.** İşletmenin kendi sitesinde kendi hakkındaki
  yorumları işaretlemesi Google'ın "self-serving reviews" politikasına girer;
  `LegalService` gibi Organization türlerinde yıldızlı sonuç verilmez. Bu yüzden
  sayfaya bilerek `aggregateRating` işaretlemesi eklenmemiştir.
