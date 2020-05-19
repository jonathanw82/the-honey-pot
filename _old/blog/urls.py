from django.urls import path
from .import views

urlpatterns = [
    path('get_blogs/', views.get_blogs, name='get_blogs'),
    path('blog_detail/<pk>', views.blog_detail, name='blog_detail'),
    path('createblog/', views.createblog_or_editblog_blog, name='createblog'),
    path('editblog/<pk>', views.createblog_or_editblog_blog, name='editblog'),
    path('blog_delete/<pk>', views.blog_delete, name='blog_delete')
]
