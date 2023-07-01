import django_filters
from .models import Expense, Income


class ExpenseFilter(django_filters.FilterSet):
    cost = django_filters.NumberFilter()
    cost__gt = django_filters.NumberFilter(field_name='cost', lookup_expr='gt')
    cost__lt = django_filters.NumberFilter(field_name='cost', lookup_expr='lt')

    expense_date = django_filters.DateFilter(field_name='expense_date')
    expense_date__gt = django_filters.DateFilter(field_name='expense_date', lookup_expr='gt')
    expense_date__lt = django_filters.DateFilter(field_name='expense_date', lookup_expr='lt')

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['category', 'currency', 'cost']

class IncomeFilter(django_filters.FilterSet):
    amount = django_filters.NumberFilter()
    amount__gt = django_filters.NumberFilter(field_name='amount', lookup_expr='gt')
    amount__lt = django_filters.NumberFilter(field_name='amount', lookup_expr='lt')

    income_date = django_filters.DateFilter(field_name='income_date')
    income_date__gt = django_filters.DateFilter(field_name='income_date', lookup_expr='gt')
    income_date__lt = django_filters.DateFilter(field_name='income_date', lookup_expr='lt')


    class Meta:
        model = Income
        fields = ['source', 'currency']
