from django import forms
from budget_manager.models import Currency, User, Income, Expense


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
        model = Income
        fields =["username","first_name", "last_name", "email"]


class UpdateIncomeForm(forms.ModelForm):
    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.user = user
    #     self.fields['currency'].label = "Waluta"
    #     self.fields['currency'].queryset = Expense.objects.
    #     print(self.fields["currency"].queryset)
    amount = forms.DecimalField(label="Kwota")
    income_date = forms.DateField(label="Data wpływu", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    source = forms.CharField(label="Źródło")
    # currency = forms.ChoiceField(label="Waluta", queryset=Currency.objects.all())

    class Meta:
        model = Income
        fields =["amount", "income_date", "source", "currency"]

class UpdateExpenseForm(forms.ModelForm):


    class Meta:
        model = Expense
        fields =["name", "cost", "expense_date" ,"user", "currency", "category"]