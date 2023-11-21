import pytest
from selenium import webdriver
from HarvestStoreAutomation.page_objects.login_page import LoginPage
from HarvestStoreAutomation.page_objects.account_page import AccountPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    return driver

@pytest.fixture
def account_page(login):
    account_page = AccountPage(login.driver)
    account_page.wait_for_account_page_to_load()
    return account_page


@pytest.fixture
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open("https://harvest-clothing.com.ua/login/")
    login_page.login("prencezza12@gmail.com", "Canima_222")
    return login_page

@pytest.fixture
def wait(setup):
    return WebDriverWait(setup, 20)


def actions(setup):
        driver = setup
        login_page = LoginPage(driver)


def browser():
    # This fixture provides a Selenium WebDriver instance
    driver = webdriver.Chrome()  # You can use other browser drivers as well
    yield driver
    driver.quit()  # This will be executed after the test to clean up resources


@pytest.fixture
def login_page(browser):
    # This fixture provides a LoginPage instance
    return LoginPage(browser)


@pytest.fixture
def account_page(browser):
    # This fixture provides an AccountPage instance
    return AccountPage(browser)

