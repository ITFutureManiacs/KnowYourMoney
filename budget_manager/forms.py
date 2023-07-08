from django import forms
from budget_manager.models import Currency, User


class CurrencyFilter(forms.ModelForm):
    currency_filter = forms.ModelChoiceField(queryset=Currency.objects.all(), initial="Zmień walutę")

    class Meta:
        model = Currency
        exclude = ["currency_code", "name"]


class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(
        label="Login:",
        widget=forms.TextInput(attrs={'class': 'form-control'}
                               ))
    first_name = forms.CharField(
        label="Imię:",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label="Nazwisko:",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        label="Adres Email:",
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields =["username","first_name", "last_name", "email"]