import {createClient} from '@sanity/client'
import {readFileSync} from 'node:fs'
import {fileURLToPath} from 'node:url'
import {dirname, join} from 'node:path'

const __dirname = dirname(fileURLToPath(import.meta.url))
const ROOT = join(__dirname, '..', '..')

function extractArray(src, name) {
  const start = src.indexOf(`const ${name}=[`)
  if (start === -1) throw new Error(`${name} not found`)
  const arrStart = src.indexOf('[', start)
  let depth = 0
  let i = arrStart
  while (i < src.length) {
    const ch = src[i]
    if (ch === "'" || ch === '"' || ch === '`') {
      const q = ch
      i++
      while (i < src.length && src[i] !== q) {
        if (src[i] === '\\') i++
        i++
      }
      i++
      continue
    }
    if (ch === '[') depth++
    else if (ch === ']') {
      depth--
      if (depth === 0) { i++; break }
    }
    i++
  }
  return new Function('return ' + src.slice(arrStart, i))()
}

function slugify(s) {
  const map = {ı: 'i', İ: 'i', ğ: 'g', Ğ: 'g', ü: 'u', Ü: 'u', ş: 's', Ş: 's', ö: 'o', Ö: 'o', ç: 'c', Ç: 'c'}
  return s
    .toLowerCase()
    .replace(/[ığüşöçİĞÜŞÖÇ]/g, (c) => map[c] || c)
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 80)
}

const projectId = process.env.SANITY_PROJECT_ID
const token = process.env.SANITY_TOKEN
if (!projectId || !token) {
  console.error('Set SANITY_PROJECT_ID and SANITY_TOKEN env vars before running.')
  process.exit(1)
}

const client = createClient({
  projectId,
  dataset: 'production',
  apiVersion: '2024-01-01',
  token,
  useCdn: false,
})

const trJs = readFileSync(join(ROOT, 'public', 'main.js'), 'utf8')
const enJs = readFileSync(join(ROOT, 'public', 'main-en.js'), 'utf8')

const trAreas = extractArray(trJs, 'AREAS')
const enAreas = extractArray(enJs, 'AREAS')
const trArticles = extractArray(trJs, 'ARTICLES')
const enArticles = extractArray(enJs, 'ARTICLES')
const trFaqs = extractArray(trJs, 'FAQS')
const enFaqs = extractArray(enJs, 'FAQS')

console.log(`Migrating ${trAreas.length} areas...`)
for (let i = 0; i < trAreas.length; i++) {
  const tr = trAreas[i]
  const en = enAreas[i] || {}
  await client.createOrReplace({
    _type: 'area',
    _id: `area-${i + 1}`,
    name: tr.name,
    name_en: en.name,
    shortDescription: tr.desc,
    shortDescription_en: en.desc,
    description: tr.desc,
    description_en: en.desc,
    tags: tr.tags,
    tags_en: en.tags,
    nedirTitle: tr.nedir,
    nedirTitle_en: en.nedir,
    nedirContent: tr.ned,
    nedirContent_en: en.ned,
    steps: (tr.steps || []).map((s, idx) => ({
      _key: `step-${idx + 1}`,
      _type: 'step',
      title: s[0],
      title_en: en.steps?.[idx]?.[0],
      description: s[1],
      description_en: en.steps?.[idx]?.[1],
    })),
    order: i + 1,
  })
  console.log(`  ✓ ${tr.name}`)
}

console.log(`Migrating ${trFaqs.length} FAQs...`)
for (let i = 0; i < trFaqs.length; i++) {
  const tr = trFaqs[i]
  const en = enFaqs[i] || {}
  await client.createOrReplace({
    _type: 'faq',
    _id: `faq-${i + 1}`,
    question: tr.q,
    question_en: en.q,
    answer: tr.a,
    answer_en: en.a,
    order: i + 1,
  })
  console.log(`  ✓ ${tr.q.slice(0, 50)}...`)
}

console.log(`Migrating ${trArticles.length} articles...`)
for (let i = 0; i < trArticles.length; i++) {
  const tr = trArticles[i]
  const en = enArticles[i] || {}
  await client.createOrReplace({
    _type: 'post',
    _id: `post-${i + 1}`,
    title: tr.baslik,
    title_en: en.baslik,
    slug: {_type: 'slug', current: slugify(tr.baslik)},
    summary: tr.ozet,
    summary_en: en.ozet,
    category: tr.dal,
    externalUrl: tr.url,
    publishedAt: new Date(Date.UTC(2024, 0, 1 + i)).toISOString(),
  })
  console.log(`  ✓ ${tr.baslik.slice(0, 50)}...`)
}

console.log('Creating siteSettings singleton...')
await client.createIfNotExists({
  _type: 'siteSettings',
  _id: 'siteSettings',
  mobilePhone: '+90 553 772 76 01',
  officePhone: '(0242) 244 10 66',
  email: 'avalpergermen@gmail.com',
  addressLine1: 'Toros, Atatürk Bulv. Başak Apt. No:96 D:11',
  addressLine2: 'Konyaaltı / Antalya',
  mapUrl:
    'https://maps.google.com/?q=Toros,+Atatürk+Bulv.+Başak+Apt.+No:96,+Konyaaltı/Antalya',
})
console.log('  ✓ siteSettings')

console.log('\nMigration complete.')
