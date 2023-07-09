import pytest

from accounts.models import CustomUser
from accounts.forms import UserRegistrationForm


@pytest.fixture
def fix_valid_user():
    user = {'username': 'testUsername',
            'password1': 'TestDjangoPass',
            'password2': 'TestDjangoPass',
            'email': 'test@username.com'}
    return user


@pytest.mark.django_db
def test_user_registration_success(fix_valid_user):
    form = UserRegistrationForm(fix_valid_user)
    result = form.is_valid()
    assert result is True


@pytest.mark.django_db
def test_user_registration_duplicated_username(fix_valid_user):
    CustomUser.objects.create_user(username='testUsername', email='dorothy@username.com')
    form = UserRegistrationForm(fix_valid_user)
    result = form.is_valid()
    assert result is False
    assert form.errors['username'][0] == 'Podany login jest już zajęty.'


@pytest.mark.django_db
def test_user_registration_duplicated_email(fix_valid_user):
    CustomUser.objects.create_user(username='Dorothy', email='test@username.com')
    form = UserRegistrationForm(fix_valid_user)
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
