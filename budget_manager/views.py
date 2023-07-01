import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Sum, Count, Subquery

from budget_manager.models import Expense, Source, Category, Currency


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 4 < datetime.datetime.now().hour < 19:
            greet = 'Dzień dobry'
        else:
            greet = 'Dobry wieczór'

        context['user'] = self.request.user
        context['greet'] = greet

        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = 'expenses_form.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        """Displays only categories made by currently logged user"""
        form = super(ExpenseCreateView, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses_list.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']

    def get_queryset(self):
        """Displays only objects made by currently logged user"""
        return Expense.objects.filter(user=self.request.user)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = 'expenses_update.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')
    context_object_name = 'expense'


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expenses_confirm_delete.html'
    success_url = reverse_lazy('expense-list')


class SourceCreateView(LoginRequiredMixin, CreateView):
    model = Source
    template_name = 'sources_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categories_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BalanceView(LoginRequiredMixin,TemplateView):
    template_name = "balance_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sum_PLN"] = Expense.objects.filter(currency__currency_code="PLN").filter(user=self.request.user). \
            aggregate(Sum("cost", default=0))["cost__sum"]
        context["sum_EUR"] = Expense.objects.filter(currency__currency_code="EUR").filter(user=self.request.user). \
            aggregate(Sum("cost", default=0))["cost__sum"]
        context["sum_GBP"] = Expense.objects.filter(currency__currency_code="GBP").filter(user=self.request.user). \
            aggregate(Sum("cost", default=0))["cost__sum"]
        context["sum_USD"] = Expense.objects.filter(currency__currency_code="USD").filter(user=self.request.user). \
            aggregate(Sum("cost", default=0))["cost__sum"]
        context["sum_CHF"] = Expense.objects.filter(currency__currency_code="CHF").filter(user=self.request.user). \
            aggregate(Sum("cost", default=0))["cost__sum"]
        context["list_of_categories"] = Category.objects.filter(user=self.request.user)
        context["number_of_categories"] = Category.objects.filter(user=self.request.user).aggregate(number=Count('*')) \
            ["number"]
        context["list_of_currencies"] = Currency.objects.all()



        print(context)
        return context
