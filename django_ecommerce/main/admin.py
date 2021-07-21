from django.contrib import admin

from .models import Product, Category, Vendor, Order, OrderProduct


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(OrderProduct)
