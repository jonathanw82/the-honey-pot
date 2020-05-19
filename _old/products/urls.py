from django.urls import path
from .import views

urlpatterns = [
    path('product_info/<product_id>/', views.product_info,
         name='product_info'),

    path('add_product/', views.add_product, name='add_product'),

    path('all_products_admin/', views.all_products_admin,
         name='all_products_admin'),

    path('delete/<product_id>/', views.delete, name='delete'),

    path('update_product/<product_id>/', views.update_product,
         name='update_product'),
]
