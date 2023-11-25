from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AccessoriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

MAIN_MENU_ACCESSORIES = (By.XPATH, '//ul[@class="mmenu mmenu-js"]//a[@href="https://harvest-clothing.com.ua/accessories/"]')
SUB_MENU_FOR_BACKPACKS_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/accessories/backpacks/"]')


def click_for_backpacks(self):
    self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
    self.click(self.SUB_MENU_FOR_BACKPACKS_LOCATOR)

