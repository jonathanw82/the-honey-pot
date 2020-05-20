from django import forms
from .models import Blog


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image',
                  'published_date')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'blog-form'
