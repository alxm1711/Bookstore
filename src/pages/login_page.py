from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button_xpath = '//img[@class="header-menu-icon-desk" and @alt="User"]'
        self.username_xpath = '//input[@name="username"]'
        self.password_xpath = '//input[@name="password"]'
        self.authenticate_xpath = '//button[@data-action="login"]'
        self.dashboard_slideshow = '//div[@id="header-image-slider"]'
    def open_bookstore_url(self, url):
        self.driver.get(url)

    def click_login(self):
        button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        button.click()

    def enter_username(self, username):
        field = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.username_xpath)))
        field.send_keys(username)

    def enter_password(self, password):
        field_password = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.password_xpath)))
        field_password.send_keys(password)

    def authenticate(self):
        button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.dashboard_slideshow)))
        button.click()

    def validate_dashboard(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.dashboard_slideshow)))
        count = self.driver.find_elements(By.XPATH, self.dashboard_slideshow)
        assert count > 0
