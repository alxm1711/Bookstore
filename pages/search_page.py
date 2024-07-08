import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchPage:

    def __init__(self, driver, context):
        self.context = context
        self.driver = driver
        self.search_button_xpath = '//button[@class="dropdown-toggle search-trigger"]'
        self.search_input_xpath = '//input[@name="search"]'
        self.submit_search_btn_xpath = '//button[@data-search-url]'
        self.first_book_xpath = '//div[@class="main-products product-grid"]/div[1]'
        self.order_first_book_xpath = '//div[@class="main-products product-grid"]/div[1]//a[@class="btn btn-cart"]'
        self.card_title_xpath = '//div[@class="main-products product-grid"]/div[1]//div[@class="name"]/a'

    def search_book_by_name(self, book_name):
        self.book_name = book_name
        button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.search_button_xpath)))
        button.click()

        field = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.search_input_xpath)))
        field.send_keys(book_name)

        button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.submit_search_btn_xpath)))
        button.click()

        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.card_title_xpath)))
        assert self.context.book_title == textfield.text



    def select_book(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.first_book_xpath)))
        button.click()

    def add_book_to_cart(self):
        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.card_title_xpath)))
        assert self.context.book_title == textfield.text


        button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.order_first_book_xpath)))
        button.click()

