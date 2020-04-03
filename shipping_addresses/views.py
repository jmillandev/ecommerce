from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .forms import ShippingAddressesForm

from .models import ShippingAddresses

class ShippingAddressesListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAddresses
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddresses.objects.filter(user=self.request.user).order_by('-default')


class ShippingAddressesUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddresses
    form_class = ShippingAddressesForm
    template_name = 'shipping_addresses/update.html'
    success_message = 'Dirección actualizada actualizada exitosamente'


    def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')

    def dispatch(self, request, *args, **kwargs):
        """
        Aquí hacemos las validaciones de la peticion
        """
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        
        return super(ShippingAddressesUpdateView, self).dispatch(request, *args, **kwargs)

class ShippingAddressesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddresses
    template_name = 'shipping_addresses/delete.html'
    success_url = reverse_lazy('shipping_addresses:shipping_addresses')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_addresses:shipping_addresses')

        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')

        return super(ShippingAddressesDeleteView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')
def create(request):
    form = ShippingAddressesForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_addresses = form.save(commit=False) #Retorna un instancia del modelo sin guardar en la DB
        shipping_addresses.user = request.user
        shipping_addresses.default = not request.user.has_shipping_address()
        
        shipping_addresses.save()

        messages.success(request, 'Dirección creada exitosamente')
        return redirect('shipping_addresses:shipping_addresses')

    return render(request, 'shipping_addresses/create.html',{
        'form' : form
    })

@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddresses, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    if request.user.has_shipping_address():
        request.user.shipping_address.update_default(default=False)
    shipping_address.update_default(default=True)
    return redirect('shipping_addresses:shipping_addresses')