from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import NewUserCreationForm
from .models import NewUser


class UserCreateView(CreateView):
    model = NewUser
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')
    form_class = NewUserCreationForm


class AuthView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LogoutView):
    pass
