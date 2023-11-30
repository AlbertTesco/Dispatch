from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserConfirmingEmailForm(forms.Form):
    confirmation_code = forms.CharField(max_length=12, label='Введите код верификации')
