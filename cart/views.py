from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
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


def remove_from_cart(request, item_id):
    """ A view to remove products in the shopping cart """
    try:
        product = get_object_or_404(Products, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, f'You have removed {product.name} from\
                                    the cart!')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=404)
