import pytest


@pytest.mark.parametrize(
    "url_fragments",
    [
        "/accounts/password_reset/",
        "/accounts/password_reset/done/",
        "/accounts/reset/<uidb64>/<token>/",
        "/accounts/reset/done/",
    ],
)
def test_urls_response_code_password(client, url_fragments):
    response = client.get(f"{url_fragments}")

    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_fragments",
    ["/accounts/login/", "/accounts/registration/", "/accounts/logout/"],
)
def test_urls_response_code_without_being_logged(client, url_fragments):
    response = client.get(f"{url_fragments}")

    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_fragments", ["/accounts/password_change/", "/accounts/password_change/done/"]
)
@pytest.mark.django_db
def test_urls_response_code_required_logged(
    client, user_login, new_user, url_fragments
):
    response = client.get(f"{url_fragments}")

    assert response.status_code == 200


@pytest.mark.django_db
def test_urls_response_code_required_logged_user_views(client, user_login, new_user):
    response_user_profile_update = client.get(f"/accounts/user/{new_user.id}/update/")
    response_user_profile = client.get("/accounts/user/view/")

    assert response_user_profile_update.status_code == 200
    assert response_user_profile.status_code == 200
