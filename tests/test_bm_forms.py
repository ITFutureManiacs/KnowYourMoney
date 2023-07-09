import pytest

from accounts.models import CustomUser
from budget_manager.models import Expense, Currency, Category


@pytest.mark.django_db
def test_expense_creation_success():
    CustomUser.objects.create_user(username='john', id='1')
    Category.objects.create(name='food', user_id='1')
    Currency.objects.create(name='zloty', currency_code='PLN')
    Expense.objects.create(name='potato',
                           cost='14',
                           category_id='1',
                           user_id='1',
                           currency_id='1',
                           expense_date='2023-01-01')
    print(f'id={CustomUser.objects.all()[0].id}')
    assert Expense.objects.count() == 1
