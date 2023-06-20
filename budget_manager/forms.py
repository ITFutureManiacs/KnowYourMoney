from django import forms
from budget_manager import models


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = '__all__'




# class IncomeSelectForm(forms.Form):
#     wybierz = forms.ModelChoiceField(queryset=models.Income.objects)