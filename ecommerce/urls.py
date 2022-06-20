from django.urls import path
from ecommerce.views import product_list, product_detail, cart_detail

app_name = 'ecommerce'

urlpatterns = [
    path('product/list', product_list, name='prod_list'),
    path('product/<str:name>', product_detail, name='prod_detail'),
    path('cart/', cart_detail, name='cart_detail')
]

