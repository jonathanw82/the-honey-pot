from django.shortcuts import render
from products.models import Products


def index(request):
    """ A view to display the index page """

    products = Products.objects.all()

    product_items = {
        'products': products,
    }

    return render(request, 'home/index.html', product_items)


def about(request):
    """ A view to display the about page """
    return render(request, 'home/about.html')
