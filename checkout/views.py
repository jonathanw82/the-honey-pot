from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm
from products.models import Products


def checkout(request):
    cart = request.session.get('cart', {})
    print(cart)
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment")
        print('help')
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
