from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClothingPage:
    # Add locators for elements on the clothing page
    FIRST_PRODUCT_LOCATOR = (By.XPATH, '//div[@class="prd-grid"]/div[1]//a[@class="prd-img"]')
    SECOND_PRODUCT_LOCATOR = (By.XPATH, '//div[@class="prd-grid"]/div[2]//a[@class="prd-img"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    # Add additional methods for interacting with elements on the clothing page
    def click_first_product(self):
        first_product_element = self.find_element(*self.FIRST_PRODUCT_LOCATOR)
        self.scroll_into_view(first_product_element)
        self.click_element(self.FIRST_PRODUCT_LOCATOR)

    def click_second_product(self):
        second_product_element = self.find_element(*self.SECOND_PRODUCT_LOCATOR)
        self.scroll_into_view(second_product_element)
        self.click_element(self.SECOND_PRODUCT_LOCATOR)
