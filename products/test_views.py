from django.test import TestCase


class TestViews(TestCase):

    def test_get_products_info(self):
        response = self.client.get('/all_products_admin')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products_admin.html')

    def test_get_add_droducts_admin(self):
        response = self.client.get('/add_product')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_add_droducts_update(self):
        response = self.client.get('/update_product')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update_product.html')

    def test_get_add_droducts_info(self):
        response = self.client.get('/product_info')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')
