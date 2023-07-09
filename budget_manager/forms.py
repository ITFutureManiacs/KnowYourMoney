from django import forms
from budget_manager.models import Currency, Income, Expense, Source, Category



class CurrencyFilter(forms.ModelForm):
    currency_filter = forms.ModelChoiceField(queryset=Currency.objects.all(), initial="Zmień walutę")

    class Meta:
        model = Currency
        exclude = ["currency_code", "name"]


class UpdateIncomeForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency'].label = "Waluta"
        self.fields['currency'].queryset = Currency.objects.all()
        self.fields['currency'].empty_label = "Wybierz Walutę"
        self.user = user
        self.fields['source'].label = "Żródło"
        self.fields['source'].queryset = Source.objects.filter(user=self.user)
        self.fields['source'].empty_label = "Wybierz Źródło"

    amount = forms.DecimalField(label="Kwota")
    income_date = forms.DateField(label="Data wpływu", widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Income
        fields = ["amount", "income_date", "source", "currency"]


class UpdateExpenseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['currency'].label = "Waluta:"
        self.fields['currency'].queryset = Currency.objects.all()
        self.fields['currency'].empty_label = "Wybierz Walutę"
        self.fields['category'].label = "Kategoria:"
        self.fields['category'].queryset = Category.objects.filter(user=self.user) | Category.objects.filter(user=None)
        self.fields['category'].empty_label = "Wybierz Kategorię"

    name = forms.CharField(label= "Nazwa:")
    cost = forms.DecimalField(label="Kwota:")
    expense_date = forms.DateField(label="Data wydatku:", widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ["name", "cost", "expense_date", "currency", "category"]

