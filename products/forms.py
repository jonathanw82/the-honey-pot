from django import forms
from .models import Products


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-product-form'
