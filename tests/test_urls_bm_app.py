import pytest


@pytest.mark.django_db
def test_urls_response_code_required_logged_income(client, user_logged_db_populated):
    response_income_create = client.get("/income/create/")
    response_income_view = client.get("/income/view/")
    response_income_update = client.get(
        f'/income/{user_logged_db_populated["new_income"].id}/update/'
    )
    response_income_delete = client.get(
        f'/income/{user_logged_db_populated["new_income"].id}/delete/'
    )

    assert response_income_create.status_code == 200
    assert response_income_view.status_code == 200
    assert response_income_update.status_code == 200
    assert response_income_delete.status_code == 200


@pytest.mark.django_db
def test_urls_response_code_required_logged_expense(client, user_logged_db_populated):
    response_expense_create = client.get("/expense/create/")
    response_expense_filter_view = client.get("/expense/filter/view")
    response_expense_update = client.get(
        f'/expense/{user_logged_db_populated["new_expense"].id}/update/'
    )
    response_expense_delete = client.get(
        f'/expense/{user_logged_db_populated["new_expense"].id}/delete/'
    )

    assert response_expense_create.status_code == 200
    assert response_expense_filter_view.status_code == 200
    assert response_expense_update.status_code == 200
    assert response_expense_delete.status_code == 200


@pytest.mark.parametrize("url_fragments", ["/", "/category/create/", "/source/create/"])
@pytest.mark.django_db
def test_urls_response_code_required_logged_home_category_source(
    client, user_logged_db_populated, url_fragments
):
    response = client.get(f"{url_fragments}")

    assert response.status_code == 200


@pytest.mark.django_db
def test_urls_response_code_required_logged_admin(client, admin_login):
    response_admin = client.get("/admin/")

    assert response_admin.status_code == 200
