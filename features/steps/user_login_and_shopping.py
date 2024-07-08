from behave import given, when, then

from pages.book_details_page import ViewBookPage
from pages.login_page import LoginPage
from pages.proceed_checkout_page import CheckoutPage
from pages.search_page import SearchPage
from pages.shopping_cart_page import ShoppingCart


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

@then('I should be redirected to my account section')
def step_impl(context):
    context.login_page.validate_my_account_section()

@when('I search for "{book_title}"')
def step_search_book(context, book_title):
    context.book_title = book_title
    context.search_page = SearchPage(context.driver, context)
    context.search_page.search_book_by_name(book_title)

@when('I select the book from the search results')
def step_select_result_book(context):
    context.search_page.select_book()

@when("I view the book's detail page")
def view_book_details(context):
    context.viewbook_page = ViewBookPage(context.driver, context)
    context.viewbook_page.view_book_details()

@when("I add the book to shopping cart")
def add_book_to_shopping_cart(context):
    context.viewbook_page.add_to_cart()

@when("I navigate to the shopping cart page")
def navigate_shopping_cart(context):
    context.shopping_cart = ShoppingCart(context.driver, context)
    context.shopping_cart.click_shopping_cart()
    context.shopping_cart.validate_shopping_cart_data()
    context.shopping_cart.finalize_order()

@when("I proceed to the checkout page")
def proceed_checkout_page(context):
    context.checkout_page = CheckoutPage(context.driver, context)
    context.checkout_page.click_new_adress()
    context.checkout_page.input_firstname("Test user")
    context.checkout_page.select_country()
    context.checkout_page.select_zone()
    context.checkout_page.select_method_of_shipping()
    context.checkout_page.select_method_of_payment()
    context.checkout_page.button_agreed_terms()
    context.checkout_page.button_send_order()


