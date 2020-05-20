from django.test import TestCase
from products.models import Products


class TestCartViews(TestCase):

    def test_cart_view(self):
        response = self.client.get('/cart/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_cart_add(self):
        product = Products.objects.create(name='test', quantity=1)
        response = self.client.get(f'/cart/add/{product.id}')
        self.assertEqual(response.status_code, 200)
