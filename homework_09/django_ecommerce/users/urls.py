from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views import UserCreateView, AuthView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
