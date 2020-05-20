from django.test import TestCase
from .models import Products
from django.contrib.auth.models import User


class TestModelsProducts(TestCase):

    # def setup(self):
    #     User.objects.create_user(
    #         email='test@test.com',
    #         username='test@test.com',
    #         password='test'
    #     )

    def test_Products_string_method_returns_name(self):
        product = Products.objects.create(name='Test')
        self.assertEqual(str(product), 'Test')


    # def test_item_string_method_returns_description(self):
    #     item = Products.objects.create(description='Test')
    #     self.assertEqual(str(item), 'Test')

    def test_created(self):
        product=Products(
            name='this test',
            description='this test',
            price=10,
        )
        product.save()
        self.assertTrue(product.created)
