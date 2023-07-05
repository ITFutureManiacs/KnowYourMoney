from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label="Login:", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(label="Hasło:", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }))
    error_messages = {
        "invalid_login": (
            "Proszę wpisz prawidłową nazwę użytkownika, email lub hasło. Zwróć uwagę, że "
            "pola są wrażliwe na wielkość liter."
        ),
        "inactive": "To konto jest nieaktywne."}