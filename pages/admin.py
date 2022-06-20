from django.contrib import admin
from ecommerce.models import Product

# Register your models here.

admin.site.site_title = 'Teste'
admin.site.register(Product)