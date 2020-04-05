from carts.utils import get_or_create_cart
from .utils import get_or_create_order

def validate_cart_and_order(func):
    def wrap(request, *args, **kwargs):
        cart = get_or_create_cart(request)
        order = get_or_create_order(request, cart)
        return func(request, cart, order, *args, **kwargs)
    return wrap