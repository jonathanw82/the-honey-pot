from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_review(request, product_id, pk=None):
    """ A view to createing and editing reviews """
    product = product_id
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
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
def review_back(request, product_id):
    return redirect('product_info', product_id)


@login_required
def edit_review(request, pk=None):
    """ A view to createing and editing reviews """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
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
