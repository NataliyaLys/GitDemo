
from time import sleep

import self
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ShoppingPage import ShoppingPage
from utilities.BeeyorBaseClass import BeeyorBaseClass


class TestE2E2(BeeyorBaseClass):
    def test_beeyor_end_to_end(self):
        shop = ShoppingPage(self.driver)
        shop.get_list_of_items().click()
        sleep(1)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "a[class='cart-contents']")).perform()
        sleep(1)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward']")).click().perform()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='coupon_code']").send_keys("Tojtech Automation")
        sleep(1)
        self.driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
        print(self.driver.find_element(By.XPATH, "//div[@role='alert']").text)

        self.driver.get("http://shopping.beeyor.com/checkout/")

        self.selfdriver.find_element(By.ID, "billing_first_name").send_keys("Nataliya")
        self.driver.find_element(By.ID, "billing_last_name").send_keys("Lys")
        self.selfdriver.find_element(By.ID, "billing_address_1").send_keys("1244 East 7TH Street")
        self.driver.find_element(By.ID, "billing_address_2").send_keys("D6")
        self.driver.find_element(By.XPATH, "//input[@name='billing_city']").send_keys("Brooklyn")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='billing_postcode']").send_keys("11234")
        self.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("+1(346)345-3456")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("Nata.fox@gmail.com")
        sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@name='order_comments']").send_keys(
            "Thank you for always being so careful with my packages and making sure they arrive safely. "
            "Thanks for doing a tough job so well.")
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[allow='payment *']"))
        self.driver.find_element(By.CSS_SELECTOR, "input[name='cardnumber']").send_keys("4242424242424242")
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[title='Secure expiration date input frame']"))
        self.driver.find_element(By.XPATH, "//input[@name='exp-date']").send_keys("1025")
        self.driver.switch_to.default_content()
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[title='Secure CVC input frame']"))
        self.driver.find_element(By.CSS_SELECTOR, "input[name='cvc']").send_keys("222")
        sleep(2)
        self.driver.switch_to.default_content()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-value='Place order']").click()