from django.shortcuts import render, get_object_or_404, redirect, reverse
#from django.utils import timezone
from .models import Review
#from products.models import Products
from .forms import ReviewPostForm
#from profiles.models import User_Profile
from django.contrib import messages
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from products.models import Products


@login_required
def create_review(request, product_id, pk=None):
    """ A view to createing and editing reviews """

    product = product_id
    #user = request.user
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            # review.user = User.objects.get(user=user)
            review.user = request.user
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
def edit_review(request, pk=None):
    """ A view to createing and editing reviews """
   # user = request.user.id
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            # review.user = User_Profile.objects.get(user=user)
            review.user = request.user
            review.save()
            messages.success(request, 'Your edit\
                was Successful!')
            return redirect('product_info', review.product_id)
    else:
        form = ReviewPostForm(instance=review)
        context = {
            'form': form,
        }
    return render(request, 'review/editreview.html', context)


@login_required
def review_delete(request, pk):
    """ A view to delete reviews """
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.warning(request, f'Review { review.title } was deleted!')
    return redirect('product_info', review.product_id)
