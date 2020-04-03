from django.shortcuts import render

from .utils import get_or_create_order
from .utils import breadcrumb
from carts.utils import get_or_create_cart

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request, cart)
    return render(request, 'orders/order.html', {
        'cart':cart,
        'order': order,
        'breadcrumb': breadcrumb(),
    })