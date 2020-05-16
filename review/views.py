from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Review
from .forms import ReviewPostForm
from profiles.models import User_Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from products.models import Products


def get_reviews(request, product_id):
    """ A view to get all review posts"""
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviewposts.html', context)


@login_required
def create_or_edit_review(request, product_id, pk=None):
    """ A view to createing and editing reviews """
    product = product_id
    user = request.user
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = User_Profile.objects.get(user=user)
            review.product_id = product
            review.save()
            messages.success(request, 'Your review\
                was Successful!')
            return redirect('product_info', product_id)
    else:
        form = ReviewPostForm(instance=review)
        context = {
            'form': form,
            'product': product,
        }
    return render(request, 'review/reviewpostform.html', context)


@login_required
def review_delete(request, pk):
    """ A view to delete reviews """

    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.warning(request, f'Review { review.title } was deleted!')
    return redirect(reverse('home'))
