from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service("C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python310\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://trade.thinkorswim.com/")
    request.cls.driver = driver
    yield
    driver.close()


