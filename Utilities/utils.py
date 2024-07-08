from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WebActions:
    def __init__(self, driver):
        self.driver = driver


    def click_button(self, xpath, wait_until=10):
        button = WebDriverWait(self.driver, wait_until).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    def input_value(self, xpath, value):
        field = WebDriverWait(self.driver, wait_until).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        field.send_keys(value)