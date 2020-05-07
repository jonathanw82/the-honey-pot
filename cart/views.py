from django.shortcuts import render


def cart_view(request):
    """ A view to display the Shopping cart page """
    return render(request, 'cart/cart.html')
