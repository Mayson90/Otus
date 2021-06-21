from django.http import Http404
from django.shortcuts import render
from .models import Product


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'products/index.html', {'products': products})
    else:
        raise Http404
