from django.urls import path

from . import views

app_name = 'shipping_addresses'

urlpatterns = [
    path('', views.ShippingAddressesListView.as_view(),name='shipping_addresses'),
    path('nueva', views.create,name='create'),
    path('editar/<int:pk>', views.ShippingAddressesUpdateView.as_view(),name='update'),
    path('eliminar/<int:pk>', views.ShippingAddressesDeleteView.as_view(),name='delete'),
    path('default/<int:pk>', views.default,name='default'),
]