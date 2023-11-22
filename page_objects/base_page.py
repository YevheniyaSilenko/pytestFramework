from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_element_is_presence(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def click_by_js(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].click()', el)

    def get_text(self, locator: tuple, index=1):
        self.wait_element_is_visible(locator)
        els = self.driver.find_elements(*locator)
        if len(els) < index-1:
            raise NoSuchElementException(str(locator) + f'by index=({index})')
        return els[index-1].text

    def get_elements_count(self, locator: tuple):
        self.wait_element_is_presence(locator)
        els = self.driver.find_elements(*locator)
        return len(els)

    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def scroll_into_view(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def scroll_to_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        ActionChains(self.driver).scroll_to_element(el).perform()

    def save_screenshot(self):
        self.driver.get_screenshot_as_file('screen.png')

    def local_storage_set_item(self, key, value):
        self.driver.execute_script(f'window.localStorage.setItem({key}, {value})')

    def remove_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].remove()', el)

    def get_current_url(self):
        return self.driver.current_url

    def mouse_hover(self, locator: tuple):
        hoverable = self.wait_element_is_visible(locator)
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def get_title(self):
        return self.driver.title
