from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from cart.forms import CartAddProductForm

class HomePage(ListView):
    model = Product
    template_name = 'product/main.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx



def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/product.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                         'title': 'Товар'})



class CatalogPage(ListView):
    model = Product
    template_name = 'product/katalog.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        ctx = super(CatalogPage, self).get_context_data(**kwargs)
        ctx['title'] = 'Катаолг'
        return ctx
