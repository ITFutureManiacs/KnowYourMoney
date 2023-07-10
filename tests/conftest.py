import datetime
import pytest

from accounts.models import CustomUser
from budget_manager.models import Currency, Category, Expense, Source, Income


@pytest.fixture
def new_admin_factory(db):
    def create_app_admin(
        username: str,
        password: str = None,
        first_name: str = 'firstname',
        last_name: str = 'lastname',
        email: str = 'test@mail.com',
        is_staff: str = True,
        is_superuser: str = True,
        is_active: str = True
    ):
        admin = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return admin
    return create_app_admin

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = 'firstname',
        last_name: str = 'lastname',
        email: str = 'test@mail.com',
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True
    ):
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user



@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory(username='testUsername', password='TestDjangoPass')

@pytest.fixture
def new_admin(db, new_admin_factory):
    return new_user_factory(username='testAdmin', password='TestDjangoPass')


@pytest.fixture
def user_login(client, new_user):
    # client = Client()
    return client.force_login(new_user)


@pytest.fixture
def admin_login(client, new_admin):
    # client = Client()
    return client.force_login(new_admin)


@pytest.fixture
def user_logged_db_populated(
        user_login,
        new_currency,
        new_source,
        new_category,
        new_income,
        new_expense):
    return {"user_login": user_login,
        "new_currency": new_currency,
        "new_source": new_source,
        "new_category": new_category,
        "new_income": new_income,
        "new_expense": new_expense}

@pytest.fixture
def fix_valid_register_dict():
    """assures dict for user_registration form"""
    reg_form_data = {'username': 'testUsername',
                     'password1': 'TestDjangoPass',
                     'password2': 'TestDjangoPass',
                     'email': 'test@username.com'}
    return reg_form_data


@pytest.fixture
def same_email_user(db, new_user_factory):
    return new_user_factory(username='Foo', email='test@username.com')


@pytest.fixture
def currency_factory(db):
    def create_currency(
        name: str,
        currency_code: str = str
    ):
        currency = Currency.objects.create(
            name=name,
            currency_code=currency_code
        )
        return currency
    return create_currency


@pytest.fixture
def new_currency(db, currency_factory):
    return currency_factory('złoty', 'PLN')


@pytest.fixture
def category_factory(db, new_user):
    def create_category(
        name: str,
        user=new_user
    ):
        category = Category.objects.create(
            name=name,
            user=user
        )
        return category
    return create_category


@pytest.fixture
def new_category(db, category_factory):
    return category_factory(name='AGD')


@pytest.fixture
def expense_factory(db, new_user, new_category, new_currency):
    def create_expense(
        name: str = 'testExpense',
        cost: int = 10,
        expense_date: str = datetime.datetime.today(),
        user=new_user,
        currency=new_currency,
        category=new_category
    ):
        expense = Expense.objects.create(
            name=name,
            cost=cost,
            expense_date=expense_date,
            user=user,
            currency=currency,
            category=category
        )
        return expense
    return create_expense


@pytest.fixture
def new_expense(db, expense_factory):
    return expense_factory(name='potato', cost=15)

@pytest.fixture
def source_factory(db, new_user):
    def create_source(name: str = 'testSource', user=new_user):
        source = Source.objects.create(name=name, user=user)
        return source
    return create_source

@pytest.fixture
def new_source(db,source_factory):
    return source_factory(name="testPraca")


@pytest.fixture
def income_factory(db, new_user, new_source, new_currency):
    def create_income(
        amount: int = 1000,
        income_date: str = datetime.datetime.today(),
        user=new_user,
        currency=new_currency,
        source=new_source
    ):
        income = Income.objects.create(
            amount=amount,
            income_date=income_date,
            user=user,
            currency=currency,
            source=source
        )
        return income
    return create_income


@pytest.fixture
def new_income(db, income_factory):
    return income_factory(amount=4000)

# @pytest.fixture - jak się dostać do tego błędu?!
# def new_expense_higher_value(db, expense_factory):
#     return expense_factory(name='potato', cost=123456)
