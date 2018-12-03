from api.models import Language
from api.serializers import LanguageSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):

    @staticmethod
    def create(name='', short=''):
        return Language.objects.create(name=name, short=short)


class LanguageListTestCase(BaseTestCase):
    url = reverse('language-list')

    def setUp(self):
        self.create(name='Afrikaans', short='af')
        self.create(name='Chinese (China)', short='zh-cn')
        self.create(name='English', short='en')
        self.create(name='French', short='fr')

    def test_list(self):
        response = self.client.get(self.url)

        expected = Language.objects.all()
        serialized = LanguageSerializer(expected, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_create(self):
        new_language = {'name': 'Japanese', 'short': 'jp', }
        response = self.client.post(self.url, new_language)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, new_language)


class LanguageDetailTestCase(BaseTestCase):

    def setUp(self):
        self.test_object = BaseTestCase.create(name='Japanese', short='jp')
        self.url = reverse(
            'language-detail',
            kwargs={'pk': self.test_object.pk, },
        )

    def test_retrieve(self):
        response = self.client.get(self.url)
        serialized = LanguageSerializer(self.test_object)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_update(self):
        response = self.client.put(
            self.url, {'name': 'Korean', 'short': 'ko', },
        )
        updated = Language.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), updated.name)

    def test_partial_update(self):
        response = self.client.patch(self.url, {'short': 'jpn', })
        patched = Language.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('short'), patched.short)
        self.assertEqual(self.test_object.name, patched.name)

    def test_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
