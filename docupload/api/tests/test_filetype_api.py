from api.models import FileType
from api.serializers import FileTypeSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):

    @staticmethod
    def create(name=''):
        return FileType.objects.create(name=name)


class FileTypeListTestCase(BaseTestCase):
    url = reverse('filetype-list')

    def setUp(self):
        self.create(name='Email')
        self.create(name='Excel')
        self.create(name='Others')
        self.create(name='PDF')
        self.create(name='Power Point')
        self.create(name='Word')

    def test_list(self):
        response = self.client.get(self.url)

        expected = FileType.objects.all()
        serialized = FileTypeSerializer(expected, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_create(self):
        new_filetype = {'name': 'Restricted', }
        response = self.client.post(self.url, new_filetype)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, new_filetype)


class FileTypeDetailTestCase(BaseTestCase):

    def setUp(self):
        self.test_object = BaseTestCase.create(name='Image')
        self.url = reverse(
            'filetype-detail',
            kwargs={'pk': self.test_object.pk, },
        )

    def test_retrieve(self):
        response = self.client.get(self.url)
        serialized = FileTypeSerializer(self.test_object)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_update(self):
        response = self.client.put(self.url, {'name': 'Audio', })
        updated = FileType.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), updated.name)

    def test_partial_update(self):
        response = self.client.patch(self.url, {'name': 'Audio', })
        patched = FileType.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), patched.name)

    def test_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
