
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "input[type='text']")
    password = (By.ID, "password1")
    rememberuserid = (By.XPATH, "//label[@for='rememberuserid']")
    accept = (By.CLASS_NAME, "accept")
    logout_button = (By.CSS_SELECTOR, "div[text()='Log Out']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_rememberuserid(self):
        return self.driver.find_element(*LoginPage.rememberuserid)

    def get_accept(self):
        return self.driver.find_element(*LoginPage.accept)

    def get_logout_button(self):
        return self.driver.find_element(*LoginPage.logout_button)