from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewArrivalsPage:
    # Define locators for 10 clickable elements
    SWEETSHOT1_LOCATOR = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/w-hud%D1%96-ta-sv%D1%96tshoty/sweatshirt-holliday-black"]')
    SWEETSHOT2_LOCATOR = (By.XPATH, '//a[href="https://harvest-clothing.com.ua/clothing/zhenschinam/w-kostyumi/suit-holiday-tash"]')
    CASPER3_LOCATOR = (By.XPATH, '//a[text()="CASPER" принт уява"]')

    ELEMENT4_LOCATOR = (By.XPATH, '//*[@id="el"]')
    ELEMENT5_LOCATOR = (By.XPATH, '//*[@id="element5"]')
    ELEMENT6_LOCATOR = (By.XPATH, '//*[@id="element6"]')
    ELEMENT7_LOCATOR = (By.XPATH, '//*[@id="element7"]')
    ELEMENT8_LOCATOR = (By.XPATH, '//*[@id="element8"]')
    ELEMENT9_LOCATOR = (By.XPATH, '//*[@id="element9"]')
    ELEMENT10_LOCATOR = (By.XPATH, '//*[@id="element10"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *locator):
            return self.driver.find_element(*locator)

    def navigate_to_new_arrivals_page(self):
            self.driver.get("https://harvest-clothing.com.ua/new")

    def get_page_title(self):
            return self.driver.title

    def get_title(self):
        return self.driver.title

    def click_sweetshot1(self):
        self.click_element(self.SWEETSHOT1_LOCATOR)

    def click_sweetshot2(self):
        self.click_element(self.SWEETSHOT2_LOCATOR)

    def click_casper3(self):
        self.click_element(self.CASPER3_LOCATOR)

    def click_element4(self):
        self.click_element(self.ELEMENT4_LOCATOR)

    def click_element5(self):
        self.click_element(self.ELEMENT5_LOCATOR)

    def click_element6(self):
        self.click_element(self.ELEMENT6_LOCATOR)

    def click_element7(self):
        self.click_element(self.ELEMENT7_LOCATOR)

    def click_element8(self):
        self.click_element(self.ELEMENT8_LOCATOR)

    def click_element9(self):
        self.click_element(self.ELEMENT9_LOCATOR)

    def click_element10(self):
        self.click_element(self.ELEMENT10_LOCATOR)

    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()


