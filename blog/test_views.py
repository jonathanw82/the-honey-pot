from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog


class TestViewsblog(TestCase):

    def test_get_blogs(self):
        response = self.client.get('/blog/get_blogs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='blog/blogposts.html')

    def test_blog_detail(self):
        blog = Blog.objects.create(title='test')
        response = self.client.get(f'/blog/blog_detail/{blog.pk}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='blog/blogdetail.html')

    def test_blog_create(self):
        User.objects.create(username='temporay', email='temporary@gmail.com',
                            password='secret')
        self.client.login(username='temporay', password='secret')
        response = self.client.get("/blog/createblog/", follow=True)
        self.assertEqual(response.status_code, 200)
