import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()


    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    return driver

@pytest.fixture
def account_page(login):
    account_page = AccountPage(login.driver)
    account_page.wait_for_account_page_to_load()
    return account_page

import pytest
from selenium import webdriver
from HarvestStoreAutomation.page_objects.login_page import LoginPage

@pytest.fixture
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open("https://harvest-clothing.com.ua/login/")
    login_page.login("prencezza12@gmail.com", "Canima_222")
    return login_page

import pytest
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def wait(setup):
    return WebDriverWait(setup, 20)

def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def actions(setup):
        driver = setup
        login_page = LoginPage(driver)




