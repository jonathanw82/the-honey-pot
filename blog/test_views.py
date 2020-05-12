from django.test import TestCase


class BlogTestViews(TestCase):

    def get_blogs(self):
        response = self.client.get('get_blogs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogposts.html')

    def blog_detail(self):
        response = self.client.get('blog_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogdetail.html')
