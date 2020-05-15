from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from django.contrib import messages
from products.models import Products


def cart_view(request):
    """ A view to display the Shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view to the products in the shopping cart """

    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    messages.success(request, f'You have successfully added {product.name} to\
                     the cart!')
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product
        to the specified amount """
    print('i have cart')
    #product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Update {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """ A view to remove products in the shopping cart """

    print('here')
    product = get_object_or_404(Products, pk=item_id)
    cart = request.session.get('cart', {})
    cart.pop(item_id)

    request.session['cart'] = cart
    messages.success(request, f'You have removed {product.name} from\
                                the cart!')
    return HttpResponse(status=200)
