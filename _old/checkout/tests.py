from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
