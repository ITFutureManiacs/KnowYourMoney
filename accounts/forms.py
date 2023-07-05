from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Hasła nie zgadzają się. Popraw i spróbuj ponownie"),
    }
    # password1 = forms.CharField(
    #     label=("Hasło:"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    # password2 = forms.CharField(
    #     label=("Potwierdź hasło:"),
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     strip=False,
    #     help_text=("Wprowadź takie samo hasło jak powyżej, dla potwierdzenia."),
    # )
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate', }))

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