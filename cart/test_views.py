from django.test import TestCase


class TestCartViews(TestCase):

    def test_cart_view(self):
        response = self.client.get('/cart/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
