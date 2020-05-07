from django.shortcuts import render
from products.models import Products


def index(request):
    """ A view to display the index page """

    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to display the about page """
    return render(request, 'home/about.html')
