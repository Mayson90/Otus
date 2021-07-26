from django.contrib.auth.forms import UserCreationForm

from .models import NewUser


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1', 'password2')
