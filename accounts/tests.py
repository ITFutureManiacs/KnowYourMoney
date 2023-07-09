from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
import pytest

# Create your tests here.
def test_urls_response_code_without_being_logged():
#     #Arrange:
    client = Client()

#     #Action:
#
    response_login = client.get('/accounts/login/')
    response_registration = client.get('/accounts/registration/')
    response_logout = client.post("/accounts/logout/")
    response_password_reset = client.get("/accounts/password_reset/")
    response_password_reset_done = client.get("/accounts/password_reset/done/")
    response_password_reset_token = client.get("/accounts/reset/<uidb64>/<token>/")
    response_password_reset_complete = client.get("/accounts/reset/done/")
#
#     #Assert
    assert response_login.status_code == 200
    assert response_registration.status_code == 200
    assert response_logout.status_code == 200
    assert response_password_reset.status_code == 200
    assert response_password_reset_done.status_code == 200
    assert response_password_reset_token.status_code == 200
    assert response_password_reset_complete.status_code == 200


@pytest.mark.django_db
def test_urls_response_code_required_logged():
    # Arrange
    model = get_user_model()
    test_user = model.objects.create(username="Mateusz", password="mojehaslo1234")

    test_user_pk = test_user.id

    client = Client()
    client.force_login(test_user)

    # Action
    response_password_change = client.get("/accounts/password_change/")
    response_password_change_done = client.get("/accounts/password_change/done/")
    response_user_profile = client.get('/accounts/user/view/')
    response_user_profile_update = client.get(f'/accounts/user/{test_user_pk}/update/')

    # Assert
    assert response_password_change.status_code == 200
    assert response_password_change_done.status_code == 200
    assert response_user_profile.status_code == 200
    assert response_user_profile_update.status_code == 200