from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse_lazy

from budget_manager.forms import IncomeForm
from budget_manager.models import Income

# Create your views here.

def income_added(request):
    return render(request, 'income_added.html', context={})

def income_update(request):
    return render(request, 'income_update.html', context={})

def income_delete(request):
    return render(request, 'income_delete_2.html', context={})


class IncomeCreateView(generic.FormView):
    template_name = 'income_create.html'
    form_class = IncomeForm
    success_url = reverse_lazy('income_added')

    def form_valid(self, form):
        wynik = super().form_valid(form)
        oczyszczone = form.cleaned_data
        print('============================')
        print(type(oczyszczone))
        print(dir(oczyszczone))
        print(oczyszczone)

        Income.objects.create(
            amount = oczyszczone['amount'],
            date = oczyszczone['date'],
            source_id = oczyszczone['source_id'],
            user_id = oczyszczone['user_id'],
            currency_id = oczyszczone['currency_id'],
        )

        return wynik


class IncomeReadView(generic.View):
    def get(self, request):
        return render(request,
                      template_name='income_read.html',
                      context={'revenues': Income.objects.all()})


class IncomeUpdateView(generic.UpdateView):
    template_name = 'income_create.html'
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('income_update')


class IncomeDeleteView(generic.DeleteView):
    model = Income
    success_url = reverse_lazy('income_delete_2')
    template_name = 'income_delete.html'
