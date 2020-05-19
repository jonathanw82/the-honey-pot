from django.urls import path
from .import views

urlpatterns = [
    path('create_review/<product_id>', views.create_review,
         name='create_review'),
    path('edit_review/<pk><product_id>', views.edit_review,
         name='edit_review'),
    path('review_delete/<pk>', views.review_delete, name='review_delete'),
    path('review_back/<product_id>', views.review_back, name='review_back'),
]
