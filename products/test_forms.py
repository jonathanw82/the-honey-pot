from django.test import TestCase
from .forms import Products


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = Products({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_item_name_is_not_required(self):
        form = Products({'name': 'honey'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = Products()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
