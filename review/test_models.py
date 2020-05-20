from django.test import TestCase
from .models import Review


class TestModelsReview(TestCase):

    def test_item_string_method_returns_title(self):
        item = Review.objects.create(title='Test')
        self.assertEqual(str(item.user), 'Test')

    # def test_item_string_method_returns_content(self):
    #     item = Review.objects.create(content='Test')
    #     self.assertEqual(str(item.content), 'Test')
