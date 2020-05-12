from django.urls import reverse
from django.test import TestCase


class TestViews(TestCase):

    # def get_blogs(self):
    #     response = self.client.get(reverse('get_blogs'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blogposts.html')

    # def blog_detail(self):
    #     response = self.client.get('/blog_detail')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blogdetail.html')

    def blog_create(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpostform.html')
