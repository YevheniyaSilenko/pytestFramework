import pytest
from page_objects.login_page import LoginPage
from page_objects.account_page import AccountPage
from utilities.driver_factory import DriverFactory
from utilities.config_reader import AppConfig
from page_objects.clothing_page import ClothingPage


@pytest.fixture
def create_driver():
    driver = DriverFactory(
        browser_id=AppConfig.browser_id
    ).get_driver()
    driver.maximize_window()
    driver.get(AppConfig.url)
    yield driver
    driver.quit()


@pytest.fixture
def login(create_driver):
    driver = create_driver
    driver.get(AppConfig.login_page_url)
    login_page = LoginPage(driver)
    login_page.login(login=AppConfig.login, password=AppConfig.password)
    return login_page


@pytest.fixture
def open_account_page(login):
    return AccountPage(login.driver)


@pytest.fixture
def open_clothing_page(login):
    login.driver.get(AppConfig.clothing_page_url)
    return ClothingPage(login.driver)


@pytest.fixture
def open_clothing_page_anonim(create_driver):
    driver = create_driver
    driver.get(AppConfig.clothing_page_url)
    return ClothingPage(driver)
