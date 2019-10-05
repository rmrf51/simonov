from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ['email', 'password1', ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', ]
