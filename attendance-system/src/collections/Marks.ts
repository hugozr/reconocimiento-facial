import { CollectionConfig } from 'payload/types';

const Marks: CollectionConfig = {
  slug: 'marks',
  auth: false,
  access: {
    read: () => true,
    create: () => true
  },
  admin: {
    useAsTitle: 'nickname',
  },
  fields: [
    {
      name: 'nickname',
      type: 'text',
    },
    {
      name: 'controlPoint',
      type: 'number',
    },
  ],
};

export default Marks;