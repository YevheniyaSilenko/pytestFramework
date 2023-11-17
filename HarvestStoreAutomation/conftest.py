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
