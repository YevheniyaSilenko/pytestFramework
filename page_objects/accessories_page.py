from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class AccessoriesPage(BasePage):
   def __init__(self, driver):
        super().__init__(driver)

   MAIN_MENU_ACCESSORIES = (By.XPATH, '//ul[@class="mmenu mmenu-js"]//a[@href="https://harvest-clothing.com.ua/accessories/"]')
   SUB_MENU_FOR_BACKPACKS_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/accessories/backpacks/"]')
   SUB_MENU_FOR_BAGS_LOCATOR = (By.XPATH, '//h3[@class="submenu-title"]//a[@href="https://harvest-clothing.com.ua/accessories/bags/"]')
   SUB_MENU_FOR_OTHER_LOCATOR = (By.CSS_SELECTOR, 'h3.submenu-title a[href="https://harvest-clothing.com.ua/accessories/portmone/"]')
   SUB_MENU_FOR_COLLECTIONS_LOCATOR = (By.CSS_SELECTOR, 'h3.submenu-title a[href="https://harvest-clothing.com.ua/accessories/collections/"]')
   SUB_MENU_FOR_VINTAGE_LOCATOR = (By.CSS_SELECTOR, 'ul.submenu-list a[href*="https://harvest-clothing.com.ua/accessories/collections/vintage/"]')
   ACTIVE_LOCATOR = (By.CSS_SELECTOR, 'ul.submenu-list a[href*="https://harvest-clothing.com.ua/accessories/collections/active/"]')
   SHUTTLE_LOCATOR = (By.CSS_SELECTOR, 'ul.submenu-list a[href*="https://harvest-clothing.com.ua/accessories/collections/shuttle/"]')
   CLASSIC_LOCATOR = (By.CSS_SELECTOR, 'ul.submenu-list a[href*="https://harvest-clothing.com.ua/accessories/collections/classic/"]')
   def click_for_backpacks(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SUB_MENU_FOR_BACKPACKS_LOCATOR)

   def click_for_bags(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SUB_MENU_FOR_BAGS_LOCATOR)

   def click_for_other(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SUB_MENU_FOR_OTHER_LOCATOR)

   def click_for_collections(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SUB_MENU_FOR_COLLECTIONS_LOCATOR)

   def click_for_vintage(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SUB_MENU_FOR_VINTAGE_LOCATOR)

   def click_for_active(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.ACTIVE_LOCATOR)

   def click_for_shuttle(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.SHUTTLE_LOCATOR)

   def click_for_classic(self):
       self.mouse_hover(self.MAIN_MENU_ACCESSORIES)
       self.click(self.CLASSIC_LOCATOR)
