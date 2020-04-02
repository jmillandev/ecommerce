from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Q

from .models import Product

class ProductListView(ListView):
    template_name ='index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = "Listado de Productos"
        return context

class ProductDetailView(DetailView): #id -> pk .Busqueda por default, el id lo toma de la url
    model = Product
    template_name = 'products/product.html'

class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        # el campo __icontains se traduce como un like %query%. Ejemplo:
        # SELECT * FROM products WHERE title like %query%;
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        return context