from django.test import TestCase
from .forms import OrderForm


class TestCheckoutPostForm(TestCase):

    def test_checkout_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_checkout_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_checkout_street1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_checkout_street2_is_not_required(self):
        form = OrderForm({'street_address2': 'address'})
        self.assertFalse(form.is_valid())

    def test_checkout_town_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_checkout_county_is_not_required(self):
        form = OrderForm({'county': ''})
        self.assertFalse(form.is_valid())

    def test_checkout_phone_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_checkout_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email',
                                            'phone_number', 'street_address1',
                                            'street_address2', 'town_or_city',
                                            'postcode', 'country', 'county',))
