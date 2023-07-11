from budget_manager.forms import UpdateExpenseForm, UpdateIncomeForm


def test_expense_update_success(new_expense):
    form = UpdateExpenseForm(1, {'name': 'tomato',
                                 'cost': '15.5',
                                 'expense_date': '2023-05-05',
                                 'currency': '1',
                                 'category': '1'})
    result = form.is_valid()

    assert result is True
    assert form.cleaned_data['name'] == 'tomato'


def test_expense_update_negative_cost(new_expense):
    form = UpdateExpenseForm(1, {'name': 'tomato',
                                 'cost': '-5',
                                 'expense_date': '2023-05-05',
                                 'currency': '1',
                                 'category': '1'})
    result = form.is_valid()
    assert result is False
    assert form.errors['cost'][0] == 'Wartość musi być większa od 0'


def test_expense_update_higher_value(new_expense):
    form = UpdateExpenseForm(1, {'name': 'tomato',
                                 'cost': '123456',
                                 'expense_date': '2023-05-05',
                                 'currency': '1',
                                 'category': '1'})
    result = form.is_valid()
    assert result is False
    assert form.errors['cost'][0] == 'Ensure that there are no more than 5 digits before the decimal point.'


def test_expense_update_more_decimal_places(new_expense):
    form = UpdateExpenseForm(1, {'name': 'tomato',
                                 'cost': '12.2222',
                                 'expense_date': '2023-05-05',
                                 'currency': '1',
                                 'category': '1'})
    result = form.is_valid()
    assert result is False
    assert form.errors['cost'][0] == 'Ensure that there are no more than 2 decimal places.'
