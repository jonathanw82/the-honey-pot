from django.test import TestCase
from .models import Products


class TestModelsProducts(TestCase):

    def test_Products_string_method_returns_name(self):
        product = Products.objects.create(name='Test')
        self.assertEqual(str(product), 'Test')

    def test_created(self):
        product = Products(
            name='this test',
            description='this test',
            price=10,
        )
        product.save()
        self.assertTrue(product.created)
