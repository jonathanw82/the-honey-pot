from django.shortcuts import render

from .models import Products


def products(request):
    """ A view to display all the products page """

    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
