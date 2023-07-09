import pytest

from accounts.models import CustomUser
from accounts.forms import UserRegistrationForm


@pytest.fixture
def fixture_1():
    user = {'username': 'testUsername',
            'password1': 'TestDjangoPass',
            'password2': 'TestDjangoPass',
            'email': 'test@username.com'}
    return user


@pytest.mark.django_db
def test_user_registration_success(fixture_1):
    form = UserRegistrationForm(fixture_1)
    result = form.is_valid()
    assert result is True


@pytest.mark.django_db
def test_user_registration_duplicated_username(fixture_1):
    CustomUser.objects.create_user(username='testUsername', email='dorothy@username.com')
    form = UserRegistrationForm(fixture_1)
    result = form.is_valid()
    assert result is False
    assert form.errors['username'][0] == 'Podany login jest już zajęty.'


@pytest.mark.django_db
def test_user_registration_duplicated_email(fixture_1):
    CustomUser.objects.create_user(username='Dorothy', email='test@username.com')
    form = UserRegistrationForm(fixture_1)
    result = form.is_valid()
    assert result is False
    assert form.errors['email'][0] == 'Podany adres email już istnieje'


@pytest.mark.django_db
def test_user_registration_common_password():
    form = UserRegistrationForm({'username': 'testUsername',
                                 'password1': 'Password',
                                 'password2': 'Password',
                                 'email': 'test@username.com'})
    result = form.is_valid()
    assert result is False
    assert form.errors['password2'][0] == 'To hasło jest zbyt powszechne.'
