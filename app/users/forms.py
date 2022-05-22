from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', )
        labels = {'username': 'логин', 'email': 'e-mail',}
        help_texts = {
            'username': '',
        }


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        exclude = ()
        fields = ('username', 'email',)
        labels = {'username': 'Логин', 'email': 'e-mail', }
        help_texts = {
            'username': '',
        }