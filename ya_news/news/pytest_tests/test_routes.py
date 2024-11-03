from http import HTTPStatus

import pytest
from pytest_django.asserts import assertRedirects
from pytest_lazyfixture import lazy_fixture as lf

OK = HTTPStatus.OK
NOT_FOUND = HTTPStatus.NOT_FOUND

COMMENT_DELETE = lf('comment_delete_url')
COMMENT_EDIT = lf('comment_edit_url')
NEWS_DETAIL = lf('news_detail_url')
NEWS_HOME = lf('news_home_url')
USERS_LOGIN = lf('users_login_url')
USERS_LOGOUT = lf('users_logout_url')
USERS_SIGNUP = lf('users_signup_url')

EXPECTED_URL_COMMENT_DELETE = lf('expected_for_comment_delete_url')
EXPECTED_URL_COMMENT_EDIT = lf('expected_for_comment_edit_url')

CLIENT_ANONYMOUS = lf('client')
CLIENT_AUTHOR = lf('client_author')
CLIENT_READER = lf('client_reader')


@pytest.mark.parametrize(
    'url, client_user, status',
    [
        (NEWS_HOME, CLIENT_ANONYMOUS, OK),
        (USERS_LOGIN, CLIENT_ANONYMOUS, OK),
        (USERS_LOGOUT, CLIENT_ANONYMOUS, OK),
        (USERS_SIGNUP, CLIENT_ANONYMOUS, OK),
        (NEWS_DETAIL, CLIENT_ANONYMOUS, OK),
        (COMMENT_EDIT, CLIENT_AUTHOR, OK),
        (COMMENT_DELETE, CLIENT_AUTHOR, OK),
        (COMMENT_EDIT, CLIENT_READER, NOT_FOUND),
        (COMMENT_DELETE, CLIENT_READER, NOT_FOUND),
    ]
)
def test_pages_availability_for_users(url, client_user, status):
    """Проверяет доступность страниц для различных пользователей."""
    response = client_user.get(url)
    assert response.status_code == status


@pytest.mark.parametrize(
    'url, client_user, expected_url',
    [
        (COMMENT_EDIT, CLIENT_ANONYMOUS, EXPECTED_URL_COMMENT_EDIT),
        (COMMENT_DELETE, CLIENT_ANONYMOUS, EXPECTED_URL_COMMENT_DELETE),
    ]
)
def test_pages_no_availability_for_anonymous_user(
    url, client_user, expected_url
):
    """Проверяет, что анонимного пользователя направляют на нужную страницу."""
    response = client_user.get(url)
    assertRedirects(response, expected_url)
