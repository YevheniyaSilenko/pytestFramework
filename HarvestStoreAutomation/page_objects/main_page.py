import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    WISHLIST_LOCATOR = (By.XPATH, '//*[@id="wishlist-total"]')
    ACCOUNT_LOCATOR = (By.CSS_SELECTOR, "i.icon.icon-person")
    CART_LOCATOR = (By.CSS_SELECTOR, "#cart-total > i")
    INFORMATION_LOCATOR = (By.XPATH, '//a[text()="Інформація"]')
    CONTACTS_LOCATOR = (By.XPATH, '//a[text()="Контакти"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def navigate_to_main_page(self):
        self.driver.get("https://harvest-clothing.com.ua/")

    def get_page_title(self):
        return self.driver.title

    def click_wishlist(self):
        self.click_element(self.WISHLIST_LOCATOR)

    def click_account(self):
        self.click_element(self.ACCOUNT_LOCATOR)

    def click_cart(self):
        self.click_element(self.CART_LOCATOR)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_contacts(self):
        # Scroll to the "Контакти" element
        contacts_element = self.find_element(*self.CONTACTS_LOCATOR)
        self.scroll_into_view(contacts_element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CONTACTS_LOCATOR)).click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

    def click_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        return self.driver.title

# Usage example:
# driver = WebDriver()  # Initialize your WebDriver instance
# main_page = MainPage(driver)
# main_page.click_contacts()
