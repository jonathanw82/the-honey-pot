
from django.test import TestCase


class TestViewsblog(TestCase):

    # def test_blog_create(self):
    #     response = self.client.get("create/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blogpostform.html')


    # def get_blogs(self):
    #     response = self.client.get(reverse('get_blogs'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blogposts.html')

    def test_blog_detail(self):
        response = self.client.get(reverse("blog_detail"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogdetail.html')
