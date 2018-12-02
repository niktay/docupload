from api.models import Confidentiality
from api.serializers import ConfidentialitySerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):

    @staticmethod
    def create(name=''):
        return Confidentiality.objects.create(name=name)


class ConfidentialityListTestCase(BaseTestCase):
    url = reverse('confidentiality-list')

    def setUp(self):
        self.create(name='Top Secret')
        self.create(name='Secret')
        self.create(name='Confidential')
        self.create(name='Private')
        self.create(name='Internal')
        self.create(name='Public')

    def test_list(self):
        response = self.client.get(self.url)

        expected = Confidentiality.objects.all()
        serialized = ConfidentialitySerializer(expected, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_create(self):
        new_confidentiality = {'name': 'Restricted', }
        response = self.client.post(self.url, new_confidentiality)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, new_confidentiality)


class ConfidentialityDetailTestCase(BaseTestCase):

    def setUp(self):
        self.test_object = BaseTestCase.create(name='Restricted')
        self.url = reverse(
            'confidentiality-detail',
            kwargs={'pk': self.test_object.pk, },
        )

    def test_retrieve(self):
        response = self.client.get(self.url)
        serialized = ConfidentialitySerializer(self.test_object)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_update(self):
        response = self.client.put(self.url, {'name': 'Unrestricted', })
        updated = Confidentiality.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), updated.name)

    def test_partial_update(self):
        response = self.client.patch(self.url, {'name': 'Unrestricted', })
        patched = Confidentiality.objects.get(id=self.test_object.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), patched.name)

    def test_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
