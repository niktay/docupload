from django.test import TestCase


class APITest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(APITest, cls).setUpClass()

    @classmethod
    def test_dummy(cls):
        assert True
