from selenium.webdriver.common.by import By
from HarvestStoreAutomation.page_objects.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_main_page(self):
        self.open(self.config['page_urls']['main_page'])

    def get_title(self):
        return self.driver.title

    def click_wishlist(self):
        wishlist_locator = (By.XPATH, '//*[@id="wishlist-id"]')
        self.click_element(wishlist_locator)

    def click_account(self):
        account_locator = (By.XPATH, '//*[@id="account-id"]')
        self.click_element(account_locator)

    def click_cart(self):
        cart_locator = (By.XPATH, '//*[@id="cart-id"]')
        self.click_element(cart_locator)

    def click_call(self):
        call_locator = (By.XPATH, '//*[@id="call-id"]')
        self.click_element(call_locator)

    def click_menu(self):
        menu_locator = (By.XPATH, '//*[@id="menu-id"]')
        self.click_element(menu_locator)
