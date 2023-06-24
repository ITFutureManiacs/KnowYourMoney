from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from budget_manager.models import Expense, Source, Category, Income


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = 'expenses_form.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses_list.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']


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



class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = 'income_form.html'
    fields = ['amount', 'source', 'income_date', 'currency']
    success_url = reverse_lazy('income-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'income_list.html'
    fields = ['amount', 'source', 'income_date', 'currency']


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    template_name = 'income_update.html'
    fields = ['amount', 'source', 'income_date', 'currency']
    success_url = reverse_lazy('income-list')
    context_object_name = 'income'


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = 'income_confirm_delete.html'
    success_url = reverse_lazy('income-list')
