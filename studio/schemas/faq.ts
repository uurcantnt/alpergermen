import {defineType, defineField} from 'sanity'

export default defineType({
  name: 'faq',
  title: 'SSS (FAQ)',
  type: 'document',
  groups: [
    {name: 'tr', title: 'Türkçe', default: true},
    {name: 'en', title: 'English'},
  ],
  fields: [
    defineField({
      name: 'question',
      title: 'Soru (TR)',
      type: 'string',
      group: 'tr',
      validation: (r) => r.required(),
    }),
    defineField({
      name: 'question_en',
      title: 'Question (EN)',
      type: 'string',
      group: 'en',
    }),
    defineField({
      name: 'answer',
      title: 'Cevap (TR)',
      type: 'text',
      rows: 5,
      group: 'tr',
      validation: (r) => r.required(),
    }),
    defineField({
      name: 'answer_en',
      title: 'Answer (EN)',
      type: 'text',
      rows: 5,
      group: 'en',
    }),
    defineField({
      name: 'order',
      title: 'Sıra',
      type: 'number',
      initialValue: 0,
    }),
  ],
  preview: {select: {title: 'question', subtitle: 'order'}},
  orderings: [
    {title: 'Sıra (artan)', name: 'orderAsc', by: [{field: 'order', direction: 'asc'}]},
  ],
})
