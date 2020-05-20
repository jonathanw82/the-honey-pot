from django.test import TestCase
from .forms import User_Profile_form


class TestProfilePostForm(TestCase):

    def test_profile_name_is_required(self):
        form = User_Profile_form({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_profile_street1_is_required(self):
        form = User_Profile_form({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_profile_street2_is_required(self):
        form = User_Profile_form({'street_address2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address2', form.errors.keys())
        self.assertEqual(form.errors['street_address2'][0],
                         'This field is required.')

    def test_profile_town_is_required(self):
        form = User_Profile_form({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_profile_county_is_required(self):
        form = User_Profile_form({'county': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('county', form.errors.keys())
        self.assertEqual(form.errors['county'][0], 'This field is required.')

    def test_profile_phone_is_required(self):
        form = User_Profile_form({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_profile_dob_is_required(self):
        form = User_Profile_form({'dob': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('dob', form.errors.keys())
        self.assertEqual(form.errors['dob'][0], 'This field is required.')

    def test_profile_fields_are_explicit_in_form_metaclass(self):
        form = User_Profile_form()
        self.assertEqual(form.Meta.fields, ['full_name', 'street_address1',
                                            'street_address2', 'town_or_city',
                                            'county', 'postcode',
                                            'phone_number', 'dob'])
