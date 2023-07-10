from budget_manager.models import Expense


def test_expense_creation_success(new_expense):
    assert Expense.objects.count() == 1
    assert new_expense.name == 'potato'


# def test_expense_creation_higher_value(new_expense_higher_value):
#     assert Expense.objects.count() == 1

