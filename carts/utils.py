from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if not cart:
        cart = Cart.objects.create(user=user)
    
    if user and not cart.user:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id
    return cart