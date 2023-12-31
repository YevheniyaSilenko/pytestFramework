import sys
import os
import json
import pytest
import constants
from constants import ROOT_PATH
import utilities.config_reader
import utilities.config_reader
from db.sqlite_pack.products_repo import ProductsRepo
from page_objects.accessories_page import AccessoriesPage
from page_objects.account_page import AccountPage
from page_objects.clothing_page import ClothingPage
from page_objects.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.json_to_dict import DictToClass

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='Choose your env')
    parser.addoption('--hub', action='store', default='False', help='Run test in container Selenoid')
    parser.addoption('--headless', action='store', default='False', help='Run test in headless mode')
    parser.addoption('--browser', action='store', default='1', help='Choose yor browser (1- chrome, 2 -firefox)')


@pytest.fixture(scope='module')
def products_repo(env):
    return ProductsRepo(f"{constants.ROOT_PATH}{env.db_param['path']}")


def fake_ware(fake):
    data = {
        "age": fake.pyint(18, 60),
        "address": fake.country(),
        "salary": float(fake.pyint(10000, 60000))
    }
    return data


@pytest.fixture(scope='session')
def env(request):
    _env_name = request.config.getoption('--env')
    with open(f'{constants.ROOT_PATH}/configs/{_env_name}.json') as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)
