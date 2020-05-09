from django.shortcuts import render
from products.models import Products
from django.contrib import messages


def index(request):
    """ A view to display the index page """

    products = Products.objects.all()

    product_items = {
        'products': products,
    }

    return render(request, 'home/index.html', product_items)


def about(request):
    """ A view to display the about page """
    messages.success(request, 'I am here!')
    return render(request, 'home/index.html')
