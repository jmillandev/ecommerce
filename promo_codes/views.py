from django.shortcuts import render

from django.http import JsonResponse

from .models import PromoCode

from orders.decorators import validate_cart_and_order

@validate_cart_and_order
def validate(request,cart, order):
    code = request.GET.get('code')
    promo_code = PromoCode.get_valid(code)

    if not promo_code:
        return JsonResponse({
            'status' : False,
            'message' : 'Codido promocional invalido',
        }, status=404)

    if promo_code.used:
        return JsonResponse({
            'status' : False,
            'message' : 'El codigo ya fue utilizado.',
        }, status=409)

    order.apply_promo_code(promo_code)

    return JsonResponse({
        'status' : True,
        'message' : 'Codigo aplicado correctamente',
        'code' : promo_code.code,
        'discount': promo_code.discount,
        'total' : order.total,
    })