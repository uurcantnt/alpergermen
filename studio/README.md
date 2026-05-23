# Alper Germen — Sanity Studio

Bu klasör, sitenin içerik yönetim panelidir. Site sahibi yazıları, SSS,
çalışma alanları ve iletişim bilgisini buradan düzenler.

## Kurulum (tek seferlik)

### 1. Sanity hesabı ve proje

1. https://www.sanity.io/manage → "Sign up"
2. "Create new project" → İsim: `Alper Germen`
3. Dataset: `production` (varsayılan)
4. Dashboard'dan **Project ID**'yi alın (8 karakter)

### 2. API token oluştur (sadece migration için)

1. Aynı dashboard'da: API → Tokens → "Add API token"
2. İsim: `migration`, izin: `Editor`
3. Tokeni kopyalayın (bir kez gösterilir)

### 3. Bağımlılıkları kur

```bash
cd studio
npm install
```

### 4. Project ID'yi tanımla

```bash
export SANITY_STUDIO_PROJECT_ID="abc12345"   # senin Project ID'in
```

### 5. Mevcut içeriği aktar

```bash
export SANITY_PROJECT_ID="abc12345"
export SANITY_TOKEN="sk_..."
npm run migrate
```

Bu, `public/main.js` ve `public/main-en.js` içindeki Çalışma Alanları,
Yazılar, SSS ve İletişim Bilgisi'ni Sanity'ye yükler. **Bir kez çalıştırılır.**

Aktarım bitince migration tokenini Sanity dashboard'undan silebilirsiniz.

### 6. Studio'yu yayına al

```bash
npm run deploy
```

Bu, paneli `https://alpergermen.sanity.studio` adresinde yayınlar.
Site sahibi bu adresten giriş yapacak.

### 7. Site sahibini ekibe davet et

Sanity dashboard → Members → Invite. Davet edilen kişi e-posta/şifre
ile (veya Google ile) panele giriş yapar.

## Şemalar

- **Çalışma Alanı** (`area`) — Hukuk dalları, anasayfa kartları ve `/alanlar` sayfası
- **Yazı** (`post`) — Blog yazıları; iç içerik veya dış bağlantı destekler
- **SSS** (`faq`) — Sıkça sorulan sorular
- **Site Ayarları** (`siteSettings`) — İletişim bilgileri (singleton, tek belge)

Her belge TR ve EN alanlarını yan yana taşır.

## Geliştirme

Yerel olarak Studio'yu çalıştırmak için:

```bash
npm run dev
```

http://localhost:3333 adresinde panel açılır.
