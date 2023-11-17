from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HarvestStoreAutomation.page_objects.base_page import BasePage

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.edit_account_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/edit-account/"]')
        self.change_password_locator = (By.CSS_SELECTOR, 'a[href="https://harvest-clothing.com.ua/change-password/"]')

        self.change_address_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/address-book/"]')
        self.orders_locator = ((By.LINK_TEXT, 'Історія замовлень'))

    def wait_for_account_page_to_load(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.edit_account_locator))
        wait.until(EC.visibility_of_element_located(self.change_password_locator))
        wait.until(EC.visibility_of_element_located(self.change_address_locator))
        wait.until(EC.visibility_of_element_located(self.orders_locator))

    def click_edit_account(self):
        self.driver.find_element(*self.edit_account_locator).click()

    def click_change_password(self):
        self.driver.find_element(*self.change_password_locator).click()

    def click_change_address(self):
        self.driver.find_element(*self.change_address_locator).click()

    def click_orders(self):
        self.driver.find_element(*self.orders_locator).click()
