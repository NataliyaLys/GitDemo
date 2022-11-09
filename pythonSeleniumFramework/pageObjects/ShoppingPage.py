import driver
from selenium.webdriver.common.by import By

class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver

    list_of_items = (By.XPATH, "//a[text()='Add to cart']")



    def get_list_of_items(self):
        list_of_items = self.driver.find_elements(*ShoppingPage.list_of_items)
        for item in list_of_items:
            item.click()
            if item == self.driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[5]"):
                break


