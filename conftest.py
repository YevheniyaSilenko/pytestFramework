import pytest
from page_objects.accessories_page import AccessoriesPage
from page_objects.login_page import LoginPage
from page_objects.account_page import AccountPage
from utilities.driver_factory import DriverFactory
import utilities.config_reader
from page_objects.clothing_page import ClothingPage
import utilities.config_reader



@pytest.fixture
def create_driver():
    driver = DriverFactory(
        browser_id=utilities.config_reader.AppConfig.browser_id
    ).get_driver()
    driver.maximize_window()
    driver.get(utilities.config_reader.AppConfig.url)
    yield driver
    driver.quit()


@pytest.fixture
def login(create_driver):
    driver = create_driver
    driver.get(utilities.config_reader.AppConfig.login_page_url)
    login_page = LoginPage(driver)
    login_page.login(login=utilities.config_reader.AppConfig.login, password=utilities.config_reader.AppConfig.password)
    return login_page


@pytest.fixture
def open_account_page(login):
    return AccountPage(login.driver)


@pytest.fixture
def open_clothing_page(login):
    login.driver.get(utilities.config_reader.AppConfig.clothing_page_url)
    return ClothingPage(login.driver)


@pytest.fixture
def open_clothing_page_anonim(create_driver):
    driver = create_driver
    driver.get(utilities.config_reader.AppConfig.clothing_page_url)
    return ClothingPage(driver)

@pytest.fixture
def open_accessories_page(login):
    login.driver.get(utilities.config_reader.AppConfig.accessories_page_url)
    return AccessoriesPage(login.driver)


