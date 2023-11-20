import self
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    WISHLIST_LOCATOR = (By.XPATH, '//*[@id="wishlist-total"]')  # Update this locator based on your HTML
    ACCOUNT_LOCATOR = (By.CSS_SELECTOR, "i.icon.icon-person")  # Update this locator based on your HTML
    CART_LOCATOR = (By.CSS_SELECTOR, "#cart-total > i")
    INFORMATION_LOCATOR = (By.XPATH, '//a[text()="Інформація"]')
 # Update this locator based on your HTML
    CONTACTS_LOCATOR = (By.XPATH, '//*[@id="Контакти"]') # Update this locator based on your HTML

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def navigate_to_main_page(self):
        self.driver.get("https://harvest-clothing.com.ua/")  # Update with your actual URL

    def get_page_title(self):
        return self.driver.title

    def click_wishlist(self):
        self.click_element(self.WISHLIST_LOCATOR)

    def click_account(self):
        self.click_element(self.ACCOUNT_LOCATOR)

    def click_cart(self):
        self.click_element(self.CART_LOCATOR)

    def click_contacts(self):
        self.click_element(self.CONTACTS_LOCATOR)

    def click_information(self):
        # Scroll to the "Інформація" element
        information_element = self.find_element(*self.INFORMATION_LOCATOR)
        self.scroll_into_view(information_element)
        self.click_element(self.INFORMATION_LOCATOR)

    def scroll_to_footer(self):
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_information_in_footer(self):
        # Scroll to the footer
        self.scroll_to_footer()


    def scroll_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

    def click_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        return self.driver.title


