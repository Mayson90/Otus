from django import template
from main.models import OrderProduct

register = template.Library()


@register.filter
def cart_product_count(user):
    #if user.is_authenticated:
    #    qs = Order.objects.filter(user=user, ordered=False)
    #    if qs.exists():
    #        return qs[0].products.count()
    #return 0
    if user.is_authenticated:
        total = 0
        try:
            order = OrderProduct.objects.filter(user=user, ordered=False)
            count = order.values('quantity')
            for i in count:
                total += i['quantity']
            return total
        except:
            return 0
