from django import forms
from .models import Products


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for field_name, field in self.fields.items():
        #     # print(field.widget)
        #     field.widget.attrs['class'] = 'border-primary rounded-0'
        #     # field.widget.attrs['placeholder'] = field_name
        #     # field.label = False