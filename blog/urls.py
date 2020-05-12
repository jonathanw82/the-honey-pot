from django.urls import path
from .import views

urlpatterns = [
    path('get_blogs/', views.get_blogs, name='get_blogs'),
    path('blog_detail/<pk>', views.blog_detail, name='blog_detail'),
    path('create/', views.create_or_edit_blog, name='create'),
    path('edit_blog/<pk>', views.create_or_edit_blog, name='edit_blog'),
    path('delete/<pk>', views.delete, name='delete')
]
