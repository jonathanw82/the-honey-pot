from django.test import TestCase
from .forms import BlogPostForm


class TestBlogPostForm(TestCase):

    def test_blog_name_is_required(self):
        form = BlogPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_blog_content_is_required(self):
        form = BlogPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BlogPostForm()
        self.assertEqual(form.Meta.fields, ('title', 'content',
                                            'image', 'published_date'))
