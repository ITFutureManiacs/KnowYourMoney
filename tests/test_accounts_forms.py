import pytest

from accounts.forms import UserRegistrationForm


@pytest.mark.django_db
def test_user_registration_success(fix_valid_register_dict):
    form = UserRegistrationForm(fix_valid_register_dict)
    result = form.is_valid()
    assert result is True


@pytest.mark.django_db
def test_user_registration_duplicated_username(fix_valid_register_dict, new_user):
    form = UserRegistrationForm(fix_valid_register_dict)
    result = form.is_valid()
    assert result is False
    assert form.errors["username"][0] == "Podany login jest już zajęty."


@pytest.mark.django_db
def test_user_registration_duplicated_email(fix_valid_register_dict, same_email_user):
    form = UserRegistrationForm(fix_valid_register_dict)
    result = form.is_valid()
    assert result is False
    assert form.errors["email"][0] == "Podany adres email już istnieje"


@pytest.mark.django_db
def test_user_registration_common_password():
    form = UserRegistrationForm(
        {
            "username": "testUsername",
            "password1": "Password",
            "password2": "Password",
            "email": "test@username.com",
        }
    )
    result = form.is_valid()
    assert result is False
    assert form.errors["password2"][0] == "To hasło jest zbyt powszechne."
