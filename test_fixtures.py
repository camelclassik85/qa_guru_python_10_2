import pytest


# @pytest.fixture(scope="session")
# def browser():
#     print("browser open")
#
#     yield
#
#     print("close browser")


@pytest.fixture
def user():
    print("user")
    return "username", "password"


@pytest.fixture
def login_page(browser):
    print("login page")


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
