import {defineType, defineField} from 'sanity'

export default defineType({
  name: 'siteSettings',
  title: 'Site Ayarları & İletişim',
  type: 'document',
  fields: [
    defineField({
      name: 'mobilePhone',
      title: 'Cep Telefonu',
      type: 'string',
      description: 'Örn: +90 553 772 76 01',
    }),
    defineField({
      name: 'officePhone',
      title: 'Sabit Telefon',
      type: 'string',
      description: 'Örn: (0242) 244 10 66',
    }),
    defineField({
      name: 'email',
      title: 'E-posta',
      type: 'string',
    }),
    defineField({
      name: 'addressLine1',
      title: 'Adres (1. satır)',
      type: 'string',
    }),
    defineField({
      name: 'addressLine2',
      title: 'Adres (2. satır)',
      type: 'string',
    }),
    defineField({
      name: 'mapUrl',
      title: 'Google Maps Bağlantısı',
      type: 'url',
    }),
  ],
  preview: {
    prepare: () => ({title: 'Site Ayarları & İletişim'}),
  },
})
