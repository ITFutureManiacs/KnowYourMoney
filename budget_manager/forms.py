from django import forms
from budget_manager.models import Currency


class CurrencyFilter(forms.ModelForm):
    currency_filter = forms.ModelChoiceField(queryset=Currency.objects.all(), initial="Zmień walutę")

    class Meta:
        model = Currency
        exclude = ["currency_code", "name"]
