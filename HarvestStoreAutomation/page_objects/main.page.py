from selenium.webdriver.common.by import By
from base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://harvest-clothing.com.ua/'

    loc_search_input = (By.ID, 'search-input')
    loc_search_btn = (By.ID, 'search-button')
    loc_cart_icon = (By.ID, 'mini-cart')
    loc_view_cart_btn = (By.XPATH, '//button[contains(text(), "View Cart")]')
    loc_new_collection = (By.XPATH, '//div[@class="featured-products"]')
    loc_product_category_menu = (By.XPATH, '//div[@class="menu-icon"]')
    loc_select_product_category = (By.XPATH, '//a[contains(text(), "Men")]')

    def search_product(self, product_name):
        self.send_keys(self.loc_search_input, product_name)
        self.click(self.loc_search_btn)

    def navigate_to_cart(self):
        self.click(self.loc_cart_icon)
        self.click(self.loc_view_cart_btn)

    def view_new_products(self):
        return self.is_displayed(self.loc_featured_products)

    def select_product_category(self):
        self.click(self.loc_product_category_menu)
        self.click(self.loc_select_product_category)
