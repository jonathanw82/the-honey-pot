from django import forms
from .models import User_Profile
from django.contrib.auth.models import User


class Logged_In_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {'username': None}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False


class User_Profile_form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['full_name', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'phone_number', 'dob', ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'phone_number': 'Phone Number',
            'dob': 'YYYY-MM-d',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields['full_name'].widget.attrs['autofocus'] = True
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False
