from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Blog
from .forms import BlogPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_blogs(request):
    """ A view to get all blog posts"""
    blogs = Blog.objects.filter(published_date__lte=timezone.now(
                                )).order_by('-published_date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blogposts.html', context)


def blog_detail(request, pk):
    """ A view to return a single post based on id """
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogdetail.html', context)


@login_required
def createblog_or_editblog_blog(request, pk=None):
    """ A view to createing and editing blogs """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can create blogs.')
        return redirect(reverse('home'))

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
            'form': form,
        }
    return render(request, 'blog/blogpostform.html', context)


@login_required
def blog_delete(request, pk):
    """ A view to delete products in admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can delete blogs.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    messages.warning(request, f'Blog Post { blog.title } was deleted!')
    return redirect(reverse('get_blogs'))
