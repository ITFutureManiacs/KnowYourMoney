from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Login lub Adres E-mail:", max_length=65)
    password = forms.CharField(label="Hasło:", max_length=65, widget=forms.PasswordInput)
