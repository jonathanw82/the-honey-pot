from django import forms
from .models import User_Profile


class User_Profile_form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['user', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'phone_number', 'dob', ]
