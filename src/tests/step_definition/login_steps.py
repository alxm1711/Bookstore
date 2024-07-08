from behave import given, when, then
from src.pages.login_page import LoginPage


@given('I open "{url}"')
def step_impl(context, url):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_bookstore_url(url)

@when('I navigate to login page')
def step_impl(context):
    context.login_page.click_login()

@when('I enter valid username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('I enter a valid password "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('I click the login button')
def step_impl(context):
    context.login_page.authenticate()

@then('I should be redirected to the dashboard')
def step_impl(context):
    context.login_page.

