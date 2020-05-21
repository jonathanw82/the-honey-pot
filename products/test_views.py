from django.test import TestCase
from django.urls import reverse
from .models import Products
from django.contrib.auth.models import User


class ProductTestViews(TestCase):

    def test_product_info(self):
        product = Products.objects.create(name="test", image="pop")
        response = self.client.get(reverse("product_info", args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')

    def test_add_products_admin(self):
        user = User.objects.create(username='temporary',
                                   email='temporary@gmail.com')
        user.set_password('secret')
        user.is_superuser = True
        user.save()
        self.client.login(username='temporary', password='secret')
        response = self.client.get(reverse("all_products_admin"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products_admin.html')

    def test_add_products_admin_login_required(self):
        user = User.objects.create(username='temporary',
                                   email='temporary@gmail.com')
        user.set_password('secret')
        user.is_superuser = True
        user.save()
        response = self.client.get(reverse("all_products_admin"))
        self.assertEqual(response.status_code, 302)

    def test_add_products_admin_superuser_required(self):
        user = User.objects.create(username='temporary',
                                   email='temporary@gmail.com')
        user.set_password('secret')
        user.is_superuser = False
        user.save()
        self.client.login(username='temporary', password='secret')
        response = self.client.get(reverse("all_products_admin"))
        self.assertEqual(response.status_code, 302)

    def test_get_products_update(self):
        user = User.objects.create(username='temporary',
                                   email='temporary@gmail.com')
        user.set_password('secret')
        user.is_superuser = True
        user.save()
        self.client.login(username='temporary', password='secret')
        product = Products.objects.create(name="test", image="pop")
        response = self.client.get(reverse("update_product",
                                   args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update_product.html')

    def test_post_products_update(self):
        user = User.objects.create(username='temporary',
                                   email='temporary@gmail.com')
        user.set_password('secret')
        user.is_superuser = True
        user.save()
        self.client.login(username='temporary', password='secret')
        product = Products.objects.create(name="test", image="pop")
        postdata = {
            'name': 'test2',
            'description': 'description',
            'price': 1.00,
            'image': 'pop'
        }
        response = self.client.post(reverse("update_product",
                                    args=[product.id]), postdata)
        product = Products.objects.get(name="test2")
        self.assertEqual(product.price, 1.00)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("all_products_admin"))
