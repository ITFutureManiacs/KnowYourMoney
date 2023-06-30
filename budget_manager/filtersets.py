import django_filters
from .models import Expense


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
