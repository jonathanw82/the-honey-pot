from django import forms
from .models import User_Profile
from django.contrib.auth.models import User


class User_Profile_form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['full_name', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'phone_number', 'dob', ]


class Logged_In_User_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


