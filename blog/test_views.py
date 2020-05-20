from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog
from django.shortcuts import reverse


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

    # def test_blog_delete(self):
    #     response = self.client.get("blog_detail/")
    #     response = self.get.redirect(reverse('get_blogs'))
    #     self.assertEqual(response.status_code, 307)


    # def test_blog_edit(self):
    #     response = self.client.get('get_blogs/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blogposts.html')

    # def test_blog_delete(self):
    #     User.objects.create(username='temporay', email='temporary@gmail.com',
    #                         password='secret')
    #     self.client.login(username='temporay', password='secret')
    #     response = self.client.get("/blog/blog_delete/", follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(template_name='blog/blogpostform.html')


    # def test_blog_delete(self):
    #     user = User.objects.create(username='testuser')
    #     user.set_password('12345')
    #     user.is_superuser = True # Optional - to set them as a superuser
    #     user.save()
    #     User =self.client.login(username='testuser', password='12345')
    #     response = self.client.get("/blog/createblog/", follow=True)
    #     self.assertEqual(response.status_code, 200)

