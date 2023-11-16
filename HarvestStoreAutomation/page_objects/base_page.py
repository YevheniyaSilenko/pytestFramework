from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://harvest-clothing.com.ua/'

    def open(self, url):
        self.driver.get(url)
        self.wait_for_page_to_load()

    def wait_element_is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not visible after {timeout} seconds.")

    def wait_for_page_to_load(self, timeout=20):

        pass

    def wait_element_is_clickable(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not clickable after {timeout} seconds.")

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)
