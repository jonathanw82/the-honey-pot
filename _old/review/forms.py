from django import forms
from .models import Review


class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content')
