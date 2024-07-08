import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutPage:

    def __init__(self, driver, context):
        self.context = context
        self.driver = driver
        self.new_adress_xpath = '//input[@value="new"]'
        self.firstname_xpath  = '//input[@id="input-payment-firstname"]'
        self.select_country_xpath = '//select[@id="input-payment-country"]'
        self.Romania_Country_xpath = '//select[@id="input-payment-country"]//option[@value="175"]'
        self.select_zone_xpath = '//select[@id="input-payment-zone"]'
        self.Bucharest_zone_xpath = '//option[@value="2688"]'
        self.shipping_method_xpath = """//div[@class='section-shipping']//div[@class="section-body"]/div[1]//input[@name='shipping_method']"""
        self.payment_method_xpath = '//input[@value="cod"]'
        self.agreed_terms_xpath = '//div[@class="checkout-section confirm-section"]//input[@type="checkbox"]'
        self.button_send_order_xpath = '//button[@id="quick-checkout-button-confirm"]'

    def click_new_adress(self):
        button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.new_adress_xpath)))
        button.click()

    def input_firstname(self, firstname):
        textfield = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.firstname_xpath)))
        textfield.send_keys(firstname)

    def select_country(self):
        select_country = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.select_country_xpath)))
        select_country.click()

        choose_Romania = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.Romania_Country_xpath)))
        choose_Romania.click()

    def select_zone(self):
        select_zone = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.select_zone_xpath)))
        select = Select(select_zone)
        select.select_by_value("2688")

    def select_method_of_shipping(self):
        select_method_of_shipping = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.shipping_method_xpath)))
        select_method_of_shipping.click()


    def select_method_of_payment(self):
        select_method_of_payment = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.payment_method_xpath)))
        select_method_of_payment.click()


    def button_agreed_terms(self):
        button_agreed_terms = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.agreed_terms_xpath)))
        button_agreed_terms.click()

    def button_send_order(self):
        button_send_order = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.button_send_order_xpath)))
        button_send_order.click()

