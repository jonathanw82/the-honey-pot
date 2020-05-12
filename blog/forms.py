from django import forms
from .models import Blog


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'profile_pic',
                  'published_date')
