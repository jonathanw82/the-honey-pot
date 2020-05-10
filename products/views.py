from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import AddProductForm
from django.contrib import messages


def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_info.html', context)


def add_product(request):
    """ A view to adding a product """

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products_admin')
        else:
            print('I am not Valid Jon Help!')

    else:
        form = AddProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


def update_product(request, product_id):
    """ A view to adding a product """
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated!')
            print('I am here!!!!!!!!!!!!!!')
            return redirect('all_products_admin')
        else:
            print('I am not Valid Jon Help!')

    else:
        form = AddProductForm(instance=product)

    context = {
        'form': form,
        'product_id': product_id,
    }
    return render(request, 'products/update_product.html', context)


def all_products_admin(request):
    """ A view to all products admin """

    product = Products.objects.all()

    context = {
        'products': product,
    }
    return render(request, 'products/all_products_admin.html', context)


@login_required
def delete(request, product_id):
    """ A view to delete products in admin """

    product = get_object_or_404(Products, pk=product_id)
    product.delete()

    return redirect(reverse('all_products_admin'))
