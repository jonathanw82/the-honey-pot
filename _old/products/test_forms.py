from django.test import TestCase
from .forms import AddProductForm


class TestProductsPostForm(TestCase):

    def test_product_name_is_required(self):
        form = AddProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_descrittion_is_required(self):
        form = AddProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_product_price_is_required(self):
        form = AddProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0],
                         'This field is required.')
