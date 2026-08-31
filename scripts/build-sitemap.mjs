#!/usr/bin/env node
/**
 * worker.js içindeki SITEMAP sabitinin <lastmod> değerlerini,
 * her sayfanın kaynak dosyasının SON COMMIT tarihinden üretir.
 *
 *   node scripts/build-sitemap.mjs           → worker.js'i günceller
 *   node scripts/build-sitemap.mjs --check   → sadece raporlar, bayat ise 1 döner
 *
 * Neden dosya sistemi tarihi (mtime) değil?
 *   CI ve Cloudflare her derlemede depoyu sıfırdan klonlar; bu durumda tüm
 *   dosyaların mtime'ı checkout anına eşitlenir ve her sayfa her deploy'da
 *   "değişmiş" görünür. Git commit tarihi ise içeriğin gerçekten değiştiği
 *   günü verir.
 *
 * URL listesi, changefreq ve priority değerleri elle yönetilmeye devam eder;
 * bu betik yalnızca <lastmod> alanına dokunur.
 */
import {readFileSync, writeFileSync, existsSync} from 'node:fs'
import {execFileSync} from 'node:child_process'

const WORKER = 'worker.js'
const ORIGIN = 'https://alpergermen.av.tr'

/* İçeriği paylaşılan bir JS paketinden gelen sayfalar: o paket değiştiğinde
   sayfanın görünen içeriği de değişir, bu yüzden tarihe dahil edilir. */
const DEPS = {
  '/': ['public/main.js'],
  '/en/': ['public/main-en.js'],
}

const check = process.argv.includes('--check')

/** URL yolundan kaynak dosyayı bulur. */
function sourceFile(path) {
  if (path === '/') return 'public/index.html'
  if (path.endsWith('/')) return `public${path}index.html`
  return `public${path}.html`
}

function git(args) {
  return execFileSync('git', args, {encoding: 'utf8'}).trim()
}

/** Çalışma ağacında değişiklik varsa dosya bugün değişmiş sayılır. */
const dirty = new Set(
  git(['status', '--porcelain'])
    .split('\n')
    .filter(Boolean)
    .map((l) => l.slice(3).trim()),
)

const today = new Date().toISOString().slice(0, 10)

function lastChanged(files) {
  const dates = []
  for (const f of files) {
    if (!existsSync(f)) continue
    if (dirty.has(f)) { dates.push(today); continue }
    const d = git(['log', '-1', '--format=%cs', '--', f])
    dates.push(d || today)
  }
  return dates.length ? dates.sort().at(-1) : today
}

let src = readFileSync(WORKER, 'utf8')
const block = src.match(/const SITEMAP = `([\s\S]*?)`;/)
if (!block) { console.error('worker.js içinde SITEMAP sabiti bulunamadı.'); process.exit(2) }

const changes = []
const missing = []

const updated = block[1].replace(/<url>[\s\S]*?<\/url>/g, (entry) => {
  const loc = entry.match(/<loc>([^<]+)<\/loc>/)?.[1]
  const old = entry.match(/<lastmod>([^<]+)<\/lastmod>/)?.[1]
  if (!loc || !old) return entry

  const path = loc.replace(ORIGIN, '') || '/'
  const file = sourceFile(path)
  if (!existsSync(file)) { missing.push([path, file]); return entry }

  const next = lastChanged([file, ...(DEPS[path] || [])])
  if (next !== old) changes.push([path, old, next])
  return entry.replace(`<lastmod>${old}</lastmod>`, `<lastmod>${next}</lastmod>`)
})

if (missing.length) {
  console.log(`\nKaynak dosyası bulunamayan ${missing.length} URL (atlandı):`)
  for (const [p, f] of missing) console.log(`  ${p}  →  ${f}`)
}

if (!changes.length) {
  console.log('sitemap güncel — değişiklik yok.')
  process.exit(0)
}

console.log(`\n${changes.length} sayfanın lastmod değeri güncel değil:`)
for (const [p, o, n] of changes) console.log(`  ${p.padEnd(56)} ${o} → ${n}`)

if (check) {
  console.log('\n--check modu: worker.js yazılmadı. Güncellemek için betiği bayraksız çalıştırın.')
  process.exit(1)
}

writeFileSync(WORKER, src.replace(block[1], updated))
console.log(`\nworker.js güncellendi (${changes.length} lastmod).`)
