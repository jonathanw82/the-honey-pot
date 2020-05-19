from django.test import TestCase
from django.urls import reverse
from .models import Products
from django.db import models


class ProductTestViews(TestCase):

    def test_get_products_info(self):
        response = self.client.get(reverse("all_products_admin"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products_admin.html')

    def test_get_add_droducts_admin(self):
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_add_droducts_update(self):
        product = Products.objects.create(name="test")

        response = self.client.get("/product_info/1/")
        self.assertEqual(response.status_code, 200)

    def test_get_add_droducts_info(self):
        response = self.client.get("/product_info")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')
