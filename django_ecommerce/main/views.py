from django.views.generic import ListView, DetailView
from .models import Product, Vendor, Order, OrderProduct
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect


class HomeView(ListView):
    model = Vendor
    template_name = 'home.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3


class VendorsListView(ListView):
    model = Product
    template_name = 'products/vendors.html'

    # def get_queryset(self):
    #     object_list = Product.objects.select_related('vendor')
    #     return object_list.filter(pk__in=[1, 2, 3, 4, 5, 6])
    #     # return Product.objects.select_related('vendor').distinct()


class CategoryListView(ListView):
    model = Product
    template_name = 'products/categories.html'

    # def get_queryset(self):
    #     object_list = Product.objects.select_related('category')
    #     return object_list.filter(pk__in=[1, 2, 3, 4])


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class VendorDetailsListView(ListView):
    model = Product
    template_name = 'products/vendor_detail.html'

    # def get(self, *args, **kwargs):
    #     self.vendor_id = kwargs['vendor_id']
    #     return super().get(*args, **kwargs)
    #
    # def get_queryset(self):
    #     return Product.objects.filter(vendor__id=self.vendor_id)


class CategoryDetailsListView(ListView):
    model = Product
    template_name = 'products/category_detail.html'

    # def get(self, *args, **kwargs):
    #     self.category_id = kwargs['category_id']
    #     return super().get(*args, **kwargs)
    #
    # def get_queryset(self):
    #     return Product.objects.filter(category__id=self.category_id)


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
            return redirect("main:products")
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
            return redirect("main:products")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
        return redirect("main:products")


@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "This product was removed from your cart.")
            return redirect("main:products")
        else:
            messages.info(request, "This product was not in your cart")
            return redirect("main:products", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("main:products", slug=slug)
