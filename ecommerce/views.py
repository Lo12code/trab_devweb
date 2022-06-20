from django.shortcuts import render
from ecommerce.models import Product, Cart

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'product/products_list.html', context)


def product_detail(request, name=None):
    print(request.user.id)
    product = Product.objects.get(name=name)

    context = {
        'product': product
    }
    return render(request, 'product/products_detail.html', context)


def cart_detail(request, client=None):
    cart = Cart.objects.get(cart_user__id=request.user.id)
    
    context = {
        'cart': cart
    }
    return render(request, 'cart/cart_detail.html', context)


