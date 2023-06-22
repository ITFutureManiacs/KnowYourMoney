from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from budget_manager.models import Expenses, Sources, Categories


class HomePageView(TemplateView):
    template_name = 'home.html'


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        form.instance.name = cleaned['name']
        form.instance.cost = cleaned['cost']
        form.instance.expense_date = cleaned['expense_date']
        form.instance.currency = cleaned['currency']
        form.instance.category = cleaned['category']
        return super().form_valid(form)


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expenses
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expenses
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expenses
    success_url = reverse_lazy('expense-list')


class SourceCreateView(LoginRequiredMixin, CreateView):
    model = Sources
    fields = ['source_name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        form.instance.source_name = cleaned['source_name']

        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    fields = ['category_name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        form.instance.category_name = cleaned['category_name']

        return super().form_valid(form)