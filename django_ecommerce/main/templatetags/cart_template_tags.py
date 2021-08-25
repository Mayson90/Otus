from django import template

from main.models import OrderProduct, Order

register = template.Library()


@register.filter
def cart_product_count(user):
    if user.is_authenticated:
        total = 0
        try:
            qs = Order.objects.filter(user=user, ordered=False)
            count = qs[0].products.values('quantity')
            for i in count:
                total += i['quantity']
            if qs.exists():
                return total
        except:
            return 0
