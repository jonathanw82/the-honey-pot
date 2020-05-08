from django.shortcuts import render, get_object_or_404
from .models import Products
from .forms import ProductForm


def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)


def add_product(request):
    """ A view to adding a product """
    form = ProductForm()

    return render(request, 'products/add_product.html', {'product_form': form})


def product_admin(request):
    """ A view to product admin """

    return render(request, 'products/product_admin.html')
