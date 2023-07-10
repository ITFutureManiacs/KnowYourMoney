import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from budget_manager.models import Expense, Income, Currency, Source, Category

@pytest.mark.django_db
def test_urls_response_code_required_logged_income_conftest(client, user_logged_db_populated):
    # Action
    response_income_create = client.get('/income/create/')
    response_income_view = client.get('/income/view/')
    response_income_update = client.get(f'/income/{user_logged_db_populated["new_income"].id}/update/')
    response_income_delete = client.get(f'/income/{user_logged_db_populated["new_income"].id}/delete/')

    # Assert
    assert response_income_create.status_code == 200
    assert response_income_view.status_code == 200
    assert response_income_update.status_code == 200
    assert response_income_delete.status_code == 200
@pytest.mark.django_db
def test_urls_response_code_required_logged_income():
    # Arrange
    model = get_user_model()

    test_user = model.objects.create(username="Mateusz", password="mojehaslo1234")

    test_currency = Currency.objects.create(name="Złoty", currency_code="PLN")

    test_source = Source.objects.create(name="Praca1", user=test_user)

    test_income = Income.objects.create(amount=100, income_date="2023-07-08", source=test_source,
                                        user=test_user, currency=test_currency)

    client = Client()
    client.force_login(test_user)

    # Action
    response_income_create = client.get('/income/create/')
    response_income_view = client.get('/income/view/')
    response_income_update = client.get(f'/income/{test_income.id}/update/')
    response_income_delete = client.get(f'/income/{test_income.id}/delete/')

    # Assert
    assert response_income_create.status_code == 200
    assert response_income_view.status_code == 200
    assert response_income_update.status_code == 200
    assert response_income_delete.status_code == 200

@pytest.mark.django_db
def test_urls_response_code_required_logged_expense():
    # Arrange
    model = get_user_model()

    test_user = model.objects.create(username="Mateusz", password="mojehaslo1234")

    test_currency = Currency.objects.create(name="Złoty", currency_code="PLN")

    test_category = Category.objects.create(name="AGD", user=test_user)

    test_expense = Expense.objects.create(name="Kawa", cost=10, expense_date="2023-07-08",
                                          user=test_user, currency=test_currency, category=test_category)

    client = Client()
    client.force_login(test_user)

    # Action
    response_expense_create = client.get('/expense/create/')
    response_expense_filter_view = client.get('/expense/filter/view')
    response_expense_update = client.get(f'/expense/{test_expense.id}/update/')
    response_expense_delete = client.get(f'/expense/{test_expense.id}/delete/')

    # Assert
    assert response_expense_create.status_code == 200
    assert response_expense_filter_view.status_code == 200
    assert response_expense_update.status_code == 200
    assert response_expense_delete.status_code == 200
@pytest.mark.django_db
def test_urls_response_code_required_logged_home_category_source():
    # Arrange
    model = get_user_model()

    test_user = model.objects.create(username="Mateusz", password="mojehaslo1234")

    test_currency = Currency.objects.create(name="Złoty", currency_code="PLN")

    client = Client()
    client.force_login(test_user)

    # Action

    response_home = client.get('/')
    response_category_create = client.get('/category/create/')
    response_source_create = client.get('/source/create/')

    # Assert

    assert response_home.status_code == 200
    assert response_category_create.status_code == 200
    assert response_source_create.status_code == 200

@pytest.mark.django_db
def test_urls_response_code_required_logged_admin():
    # Arrange
    model = get_user_model()

    test_super_user = model.objects.create(username="Admin", password="test", is_superuser=1, is_staff=1)

    client = Client()

    client.force_login(test_super_user)

    # Action
    response_admin = client.get('/admin/')

    # Assert
    assert response_admin.status_code == 200