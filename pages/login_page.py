import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_xpath = """/html/body/div[4]/header/div[1]/div[2]/div[3]/div[1]/div/ul/li[1]/a"""
        self.signin_button_xpath = """//a[@class=" rhf-sign-in rhf-myaccount-menu-item btn btn--medium"]"""
        self.username_xpath = '//input[@id="input-email"]'
        self.password_xpath = '//input[@id="input-password"]'
        self.authenticate_xpath = """//button[@data-loading-text="<span>Autentificare</span>"]"""
        self.my_acc_section_xpath = '//h2[@class="title" and text()="Contul Meu"]'
        self.accept_all_cookies_btn = '//button[@id="onetrust-accept-btn-handler"]'

    def open_bookstore_url(self, url):
        self.driver.get(url)



    def click_login(self):
        # time.sleep(1232131)
        button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.my_account_xpath)))
        button.click()

        # button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.signin_button_xpath)))
        # button.click()
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def enter_username(self, username):
        time.sleep(2)
        field = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.username_xpath)))
        field.send_keys(username)

    def enter_password(self, password):
        field_password = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.password_xpath)))
        field_password.send_keys(password)

    def authenticate(self):
        button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.authenticate_xpath)))
        button.click()

    def validate_my_account_section(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.my_acc_section_xpath)))
        count = len(self.driver.find_elements(By.XPATH, self.my_acc_section_xpath))
        assert count > 0, "My account H2 title not found"
