from django.shortcuts import render
from ecommerce.models import Product

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'product/products_list.html', context)