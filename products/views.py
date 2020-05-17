from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Products
from review.models import Review
from .forms import AddProductForm
from django.contrib import messages
from profiles.models import User_Profile


def product_info(request, product_id):
    """ A view to show individual product details """

    # reviews = Review.objects.filter(User_Profile, user=request.user)
    reviews = Review.objects.filter(product_id=product_id)
    product = get_object_or_404(Products, pk=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'products/product_info.html', context)


@login_required
def add_product(request):
    """ A view to adding a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added\
                             a new product')
            return redirect('all_products_admin')
        else:
            messages.error(request, 'Your product was not valid')
    else:
        form = AddProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


@login_required
def update_product(request, product_id):
    """ A view to adding a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product {product.name} was Updated!')
            return redirect('all_products_admin')
        else:
            messages.error(request, 'Product Was Not Updated!')
    else:
        form = AddProductForm(instance=product)
        messages.info(request, f'You are updating {product.name}!')
    context = {
        'form': form,
        'product_id': product_id,
    }
    return render(request, 'products/update_product.html', context)


@login_required
def all_products_admin(request):
    """ A view to all products admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you have no access here.')
        return redirect(reverse('home'))

    product = Products.objects.all()
    context = {
        'products': product,
    }
    return render(request, 'products/all_products_admin.html', context)


@login_required
def delete(request, product_id):
    """ A view to delete products in admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    product.delete()
    messages.warning(request, f'Product {product.name} was deleted!')
    return redirect(reverse('all_products_admin'))
