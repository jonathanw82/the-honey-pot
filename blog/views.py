from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogPostForm
from django.contrib import messages


def get_blogs(request):
    """ A view to get all blog posts"""
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blogposts.html', context)


def blog_detail(request, pk):
    """ A view to return a sigle post based on id """
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogdetail.html', context)


def create_or_edit_blog(request, pk=None):
    """ A view to createing and editing blogs """
    blog = get_object_or_404(Blog, pk=pk) if pk else None
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Your blog post\
             was Successful!')
            return redirect(blog_detail, blog.pk)
    else:
        form = BlogPostForm(instance=blog)
        context = {
            'form': form
        }
    return render(request, 'blog/blogpostform.html', context)
