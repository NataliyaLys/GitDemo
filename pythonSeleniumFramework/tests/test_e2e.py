from time import sleep

import pytest
from selenium.webdriver import Keys

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        sleep(3)
        login.get_password().send_keys(data_load["password"])
        sleep(3)
        login.get_rememberuserid().click()
        sleep(2)
        login.get_accept().click()
        sleep(2)
        trade = TradePage(self.driver)
        trade.get_trade_button().click()
        trade.get_symbol().send_keys("AAPL")
        trade.get_symbol_lookup().click()
        trade.get_side().click()
        trade.get_quantity().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(15)
        sleep(2)
        trade.get_review().click()
        trade.get_send().click()
        sleep(2)
        trade.get_notifications().click()
        sleep(2)
        trade.get_order_confirmation()
        sleep(2)
        login.get_logout_button().click()
        print("Calins changes1")
        print("Calins changes2")
        print("Calins changes3")
        print("Calins changes4")
        print("Calins changes5")
        print("Calins changes6")
        print("Calins changes7")

    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param



        # self.driver.find_element(By.ID, "username0").send_keys("tojtech111")
        # self.driver.find_element(By.ID, "password1").send_keys("Default111")
        # self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
        # self.driver.find_element(By.CLASS_NAME, "accept").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("AAPL")
        # self.driver.find_element(By.CSS_SELECTOR, "li[data-testid='symbol-search-dropdown:AAPL']").click()
        # self.driver.find_element(By.XPATH, "//button[@aria-label='Buy A A P L']").click()

        # self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='trade-quantity-input']").send_keys(Keys.CONTROL + "a")
        # self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='trade-quantity-input']").send_keys(Keys.BACK_SPACE * 3)
        # self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='trade-quantity-input']").send_keys(
        #     Keys.BACK_SPACE)
        # self.driver.find_element(By.XPATH, "//button[@data-testid='order-type-dropdown-value']").click()
        # sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, "li[data-testid='order-type-dropdown:LIMIT']").click()
        # sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Time in Force']").click()
        # sleep(2)
        # self.driver.find_element(By.XPATH, "//li[@data-testid='tif-dropdown:DAY']").click()
        # sleep(2)
        # self.driver.find_element(By.ID, "review-order-button").click()
        # sleep(2)
        # self.driver.find_element(By.ID, "send-order-button").click()
        # sleep(2)
        # self.driver.find_element(By.XPATH, "//div[text()='Notifications']").click()
