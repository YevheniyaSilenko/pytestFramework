from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ClothingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    # Add locators for elements on the clothing page
    MAIN_MENU_CLOTHING = (By.XPATH, '//ul[@class="mmenu mmenu-js"]//a[@href="https://harvest-clothing.com.ua/clothing/"]')
    SUB_MENU_FOR_WOMAN_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/"]')
    SECOND_PRODUCT_LOCATOR = (By.XPATH, '//div[@class="prd-grid"]/div[2]//a[@class="prd-img"]')

    # Add additional methods for interacting with elements on the clothing page
    def click_for_woman(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_WOMAN_LOCATOR)

    def click_second_product(self):
        self.click(self.SECOND_PRODUCT_LOCATOR)

    def is_product_details_displayed(self):
        pass

