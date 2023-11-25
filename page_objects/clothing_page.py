from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ClothingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    # Add locators for elements on the clothing page
    MAIN_MENU_CLOTHING = (By.XPATH, '//ul[@class="mmenu mmenu-js"]//a[@href="https://harvest-clothing.com.ua/clothing/"]')
    SUB_MENU_FOR_WOMAN_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/"]')
    SUB_MENU_FOR_MEN_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/clothing/muzhchinam/"]')
    SUB_MENU_FOR_X_NU_OT_LOCATOR = (By.XPATH, '//ul[@class="submenu-list"]//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/harvest-x-nu-ot-9/"]')
    SUB_MENU_FOR_SUITS_LOCATOR = (By.XPATH, '//ul[@class="submenu-list"]//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/w-kostyumi/"]')
    SUB_MENU_FOR_SHORTS_LOCATOR = (By.XPATH, '//ul[@class="submenu-list"]//a[@href="https://harvest-clothing.com.ua/clothing/muzhchinam/m-shorty/"]')
    SWEETSHOT1_LOCATOR = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/clothing/zhenschinam/w-hud%D1%96-ta-sv%D1%96tshoty/sweatshirt-holliday-black"]')
    def click_for_woman(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_WOMAN_LOCATOR)


    def click_for_men(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_MEN_LOCATOR)


    def click_for_x_nu_ot(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_X_NU_OT_LOCATOR)

    def click_for_suits(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_SUITS_LOCATOR)

    def click_for_shorts(self):
        self.mouse_hover(self.MAIN_MENU_CLOTHING)
        self.click(self.SUB_MENU_FOR_SHORTS_LOCATOR)
    def is_product_details_displayed(self):
        pass

