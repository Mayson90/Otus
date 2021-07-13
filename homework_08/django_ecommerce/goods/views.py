from django.views.generic import ListView, DetailView

from .models import Product, Vendor


# Create your views here.
class HomeView(ListView):
    model = Vendor
    template_name = 'home.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    # paginate_by = 4


class VendorsListView(ListView):
    model = Product
    template_name = 'products/vendors.html'

    def get_queryset(self):
        object_list = Product.objects.select_related('vendor')
        return object_list.filter(pk__in=[1, 2, 3, 4, 5, 6])
        # return Product.objects.select_related('vendor').distinct()


class CategoryListView(ListView):
    model = Product
    template_name = 'products/categories.html'

    def get_queryset(self):
        object_list = Product.objects.select_related('category')
        return object_list.filter(pk__in=[1, 2, 3, 4])


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class VendorDetailsListView(ListView):
    model = Product
    template_name = 'products/vendor_detail.html'

    def get(self, *args, **kwargs):
        self.vendor_id = kwargs['vendor_id']
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(vendor__id=self.vendor_id)


class CategoryDetailsListView(ListView):
    model = Product
    template_name = 'products/category_detail.html'

    def get(self, *args, **kwargs):
        self.category_id = kwargs['category_id']
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(category__id=self.category_id)
