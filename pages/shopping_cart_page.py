import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ShoppingCart:

    def __init__(self, driver, context):
        self.context = context
        self.driver = driver
        self.shopping_cart_xpath = '//i[@class="fa fa-shopping-cart"]'
        self.shopping_cart_title = '//span[contains(text(), "Coș de cumpărături")]'
        self.cart_book_title = '//form[@class="cart-table"]//tbody//tr[1]//td[@class="text-left td-name"]/a'
        self.finish_order = '//span[text()="Finalizare comandă"]'
        self.finish_the_order_xpath  = '//a[@class="btn btn-primary"]'

    def click_shopping_cart(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.finish_order)))

        button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.shopping_cart_xpath)))
        button.click()


    def validate_shopping_cart_data(self):

        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.shopping_cart_title)))

        assert 'coș de cumpărături' == textfield.text.lower()

        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.cart_book_title)))
        assert self.context.book_title.lower() == textfield.text.lower()


    def finalize_order(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.finish_the_order_xpath)))
        button.click()

