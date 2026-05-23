import {defineType, defineField} from 'sanity'

export default defineType({
  name: 'post',
  title: 'Yazı (Article)',
  type: 'document',
  groups: [
    {name: 'tr', title: 'Türkçe', default: true},
    {name: 'en', title: 'English'},
    {name: 'meta', title: 'Genel'},
  ],
  fields: [
    defineField({
      name: 'title',
      title: 'Başlık (TR)',
      type: 'string',
      group: 'tr',
      validation: (r) => r.required(),
    }),
    defineField({
      name: 'title_en',
      title: 'Title (EN)',
      type: 'string',
      group: 'en',
    }),
    defineField({
      name: 'summary',
      title: 'Özet (TR)',
      type: 'text',
      rows: 3,
      group: 'tr',
    }),
    defineField({
      name: 'summary_en',
      title: 'Summary (EN)',
      type: 'text',
      rows: 3,
      group: 'en',
    }),
    defineField({
      name: 'slug',
      title: 'URL (Slug)',
      type: 'slug',
      options: {source: 'title', maxLength: 96},
      group: 'meta',
      validation: (r) => r.required(),
    }),
    defineField({
      name: 'category',
      title: 'Hukuk Dalı',
      type: 'string',
      group: 'meta',
      options: {
        list: [
          {title: 'Aile Hukuku', value: 'Aile Hukuku'},
          {title: 'Ceza Hukuku', value: 'Ceza Hukuku'},
          {title: 'İş Hukuku', value: 'İş Hukuku'},
          {title: 'Gayrimenkul Hukuku', value: 'Gayrimenkul Hukuku'},
          {title: 'İdare Hukuku', value: 'İdare Hukuku'},
          {title: 'İcra Hukuku', value: 'İcra Hukuku'},
          {title: 'Tüketici Hukuku', value: 'Tüketici Hukuku'},
          {title: 'Ticaret Hukuku', value: 'Ticaret Hukuku'},
          {title: 'Yabancılar Hukuku', value: 'Yabancılar Hukuku'},
        ],
      },
    }),
    defineField({
      name: 'publishedAt',
      title: 'Yayın Tarihi',
      type: 'datetime',
      group: 'meta',
      initialValue: () => new Date().toISOString(),
    }),
    defineField({
      name: 'coverImage',
      title: 'Kapak Görseli',
      type: 'image',
      options: {hotspot: true},
      group: 'meta',
    }),
    defineField({
      name: 'externalUrl',
      title: 'Dış Bağlantı (opsiyonel)',
      type: 'url',
      description:
        'Dolu ise yazı kartı doğrudan bu adrese yönlenir. Boş bırakırsanız sitedeki "İçerik" alanı gösterilir.',
      group: 'meta',
    }),
    defineField({
      name: 'body',
      title: 'İçerik (TR)',
      type: 'array',
      of: [{type: 'block'}, {type: 'image', options: {hotspot: true}}],
      group: 'tr',
    }),
    defineField({
      name: 'body_en',
      title: 'Content (EN)',
      type: 'array',
      of: [{type: 'block'}, {type: 'image', options: {hotspot: true}}],
      group: 'en',
    }),
  ],
  preview: {
    select: {title: 'title', subtitle: 'category', media: 'coverImage'},
  },
  orderings: [
    {
      title: 'Yayın Tarihi (yeni → eski)',
      name: 'publishedDesc',
      by: [{field: 'publishedAt', direction: 'desc'}],
    },
  ],
})
