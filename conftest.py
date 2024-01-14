import pytest


@pytest.fixture(scope="session")
def browser():
    print("browser open")

    yield

    print("close browser")