import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from goods.views import HomeView, ProductsListView, ProductsDetailView, VendorsListView, VendorDetailsListView, \
    CategoryListView, CategoryDetailsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductsDetailView.as_view()),
    path('vendors/', VendorsListView.as_view(), name='vendors'),
    path('vendor_detail/<int:vendor_id>/', VendorDetailsListView.as_view(), name='vendor_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_detail/<int:category_id>/', CategoryDetailsListView.as_view(), name='category_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
