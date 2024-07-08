import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ViewBookPage:

    def __init__(self, driver, context):
        self.context = context
        self.driver = driver
        self.book_title_xpath = '//h1[@class="title page-title"]/span'
        self.stock_value_xpath = '//li[@class="product-stock in-stock"]/span'
        self.add_to_card_xpath = '//a[@id="button-cart"]'

    def view_book_details(self):
        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.book_title_xpath)))


        assert self.context.book_title.lower() == textfield.text.lower(), \
            f"Book title mismatch: Context title '{self.context.book_title}' != Page title '{textfield.text}'"

        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.stock_value_xpath)))
        assert 'In Stoc' == textfield.text
        #Todo - other validations like price from cart == price on details == price at checkout

    def add_to_cart(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.add_to_card_xpath)))
        button.click()
