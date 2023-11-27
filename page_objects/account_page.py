from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.edit_account_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/edit-account/"]')
        self.change_password_locator = (By.CSS_SELECTOR, 'a[href="https://harvest-clothing.com.ua/change-password/"]')
        self.change_address_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/address-book/"]')
        self.orders_locator = (By.XPATH, '//h3[contains(text(), "Історія замовлень")]')

    def click_edit_account(self):
        self.click(self.edit_account_locator)

    def click_change_password(self):
        self.click(self.change_password_locator)

    def click_change_address(self):
        self.click(self.change_address_locator)

    def click_orders(self):
        self.click(self.orders_locator)
