from django.test import TestCase
from .models import Blog


class TestModelsBlog(TestCase):

    def test_item_string_method_returns_title(self):
        item = Blog.objects.create(title='Test')
        self.assertEqual(str(item), 'Test')

    def test_item_string_method_returns_content(self):
        item = Blog.objects.create(content='Test')
        self.assertEqual(str(item.content), 'Test')

