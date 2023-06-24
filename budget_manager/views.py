from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from budget_manager.models import Expense, Source, Category


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = 'expenses_form.html'
    fields = ['name', 'cost', 'expense_date', 'currency', 'category']
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        # TODO czy można usunąć
        form.instance.name = cleaned['name']
        form.instance.cost = cleaned['cost']
        form.instance.expense_date = cleaned['expense_date']
        form.instance.currency = cleaned['currency']
        form.instance.name = cleaned['category']
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
    context_object_name = 'xyz'


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expenses_confirm_delete.html'
    success_url = reverse_lazy('expense-list')


class SourceCreateView(LoginRequiredMixin, CreateView):
    model = Source
    template_name = 'sources_form.html'
    fields = ['source_name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        form.instance.name = cleaned['source_name']

        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categories_form.html'
    fields = ['category_name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cleaned = form.cleaned_data
        form.instance.user = self.request.user
        form.instance.name = cleaned['category_name']

        return super().form_valid(form)