import django_filters
from django.forms import DateInput

from .models import Expense, Category, Income, Source


def categories_list(request):
    if request.user.is_authenticated:
        return Category.objects.filter(user=None) | Category.objects.filter(user=request.user)
    return Category.objects.none()


def sources_list(request):
    if request.user.is_authenticated:
        return Source.objects.filter(user=None) | Source.objects.filter(user=request.user)
    return Source.objects.none()


class ExpenseFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(label='Kategoria', queryset=categories_list)
    cost = django_filters.RangeFilter(label='Wartość')
    expense_date__gte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}),
                                                  label='Od', field_name='expense_date', lookup_expr='gte')
    expense_date__lte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}),
                                                  label='Do', field_name='expense_date', lookup_expr='lte')
    name = django_filters.CharFilter(label='Nazwa', lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['currency']


class IncomeFilter(django_filters.FilterSet):
    amount = django_filters.RangeFilter(label='Wartość')
    income_date__gte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}),
                                                 label='Od', field_name='expense_date', lookup_expr='gte')
    income_date__lte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}),
                                                 label='Do', field_name='expense_date', lookup_expr='lte')
    source = django_filters.ModelChoiceFilter(label='Źródło', queryset=sources_list)

    class Meta:
        model = Income
        fields = ['currency']
