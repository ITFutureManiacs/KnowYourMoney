from budget_manager.models import Expense, Income, Currency, Category, Source


def test_expense_creation_success(new_expense):
    assert Expense.objects.count() == 1
    assert new_expense.name == "potato"


def test_income_creation_success(new_income):
    assert Income.objects.count() == 1
    assert new_income.amount == 4000


def test_source_creation_success(new_source):
    assert Source.objects.count() == 1
    assert new_source.name == "testPraca"


def test_category_creation_success(new_category):
    assert Category.objects.count() == 1
    assert new_category.name == "AGD"


def test_currency_creation_success(new_currency):
    assert Currency.objects.count() == 1
    assert new_currency.name == "złoty"
    assert new_currency.currency_code == "PLN"


def test_expense_creation_higher_value(new_expense_higher_value):
    assert "Too much digits. Including decimals." == new_expense_higher_value
    assert Expense.objects.count() == 0
