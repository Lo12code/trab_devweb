from django.urls import path
from ecommerce.views import product_list

app_name = 'ecommerce'

urlpatterns = [
    path('product/list', product_list, name='prod_list'),
]

