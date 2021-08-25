from django.contrib import admin

from .models import Product, Category, Vendor, Order, OrderProduct, Payment, BillingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'billing_address',
        'payment'
    ]
    list_display_links = [
        'user',
        'billing_address',
        'payment',
    ]
    list_filter = [
        'ordered'
    ]
    search_fields = [
        'user__username'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'default'
    ]
    list_filter = ['default', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)
admin.site.register(BillingAddress, AddressAdmin)
