from django.test import TestCase
from .forms import ReviewPostForm


class TestReviewPostForm(TestCase):

    def test_review_name_is_required(self):
        form = ReviewPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_review_content_is_required(self):
        form = ReviewPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewPostForm()
        self.assertEqual(form.Meta.fields, ('title', 'content'))
