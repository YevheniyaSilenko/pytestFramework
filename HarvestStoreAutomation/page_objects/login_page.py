from selenium.webdriver.common.by import By
from HarvestStoreAutomation.page_objects.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://harvest-clothing.com.ua/login/'

    loc_username_input = (By.XPATH, '//*[@id="input-email"]')
    loc_password_input = (By.XPATH, '//*[@id="input-password"]')
    loc_login_btn = (By.CSS_SELECTOR, '#loginForm > div > form > button')

    def set_login(self, login):
        self.wait_element_is_visible(self.loc_username_input)
        self.send_keys(self.loc_username_input, login)
        return self

    def set_password(self, password):
        self.wait_element_is_visible(self.loc_password_input)
        self.send_keys(self.loc_password_input, password)
        return self

    def click_login_btn(self):
        self.wait_element_is_clickable(self.loc_login_btn)
        self.click(self.loc_login_btn)
