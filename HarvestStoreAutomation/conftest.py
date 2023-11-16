import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()


    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    return driver
