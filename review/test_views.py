from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review


class TestViewsReview(TestCase):

    # def test_review_back(self):
    #     User.objects.create(username='temporay', email='temporary@gmail.com',
    #                         password='secret')
    #     self.client.login(username='temporay', password='secret')
    #     response = self.client.get('/blog/review_back/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(template_name='product_info')

    def test_review_create(self):
        User.objects.create(username='temporay', email='temporary@gmail.com',
                            password='secret')
        self.client.login(username='temporay', password='secret')
        response = self.client.get("/review/create_review/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='review/reviewpostform.html')


    # def test_blog_create(self):
    #     user = User.objects.create(username='testuser')
    #     user.ser
    #     user.set_password('12345')
    #     user.is_superuser = True # Optional - to set them as a superuser
    #     user.save()
    #     logged_in = self.client.login(user)
    #     response = self.client.get("/review/createblog/", follow=True)


    # def test_review_create(self):
    #     review = Review.objects.create(title='test')
    #     response = self.client.get(f'/blog/blog_detail/{blog.pk}', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(template_name='blog/blogdetail.html')