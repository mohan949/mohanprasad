import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@pytest.fixture
def browser_context_args(browser_context_args):
    # You can customize browser context here if needed
    return browser_context_args

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given("I am on the login page")
def go_to_login(login_page):
    login_page.goto()

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(login_page, username, password):
    login_page.login(username, password)

@then("I should see the dashboard")
def should_see_dashboard(login_page):
    assert login_page.is_dashboard_visible()
