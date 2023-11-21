from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions, Keys
from selenium.webdriver.chrome.service import Service

_CHROME_ID = 1
_FIREFOX_ID = 2


class DriverFactory:
    def __init__(self, browser_id: int):
        self.__browser_id = browser_id

    def get_driver(self):
        if int(self.__browser_id) == _CHROME_ID:
            return self.__get_chrome_driver()
        elif int(self.__browser_id) == _FIREFOX_ID:
            return self.__get_firefox_driver()
        else:
            return self.__get_chrome_driver()

    from selenium.webdriver.chrome.service import Service

    # ...

    @staticmethod
    def __get_chrome_driver():
        _options = ChromeOptions()
        _options.browser_version = '119'

        # Вказати шлях до chromedriver через Service
        service = Service("/usr/local/bin/chromedriver")

        driver = Chrome(options=_options, service=service)
        return driver

    @staticmethod
    def __get_firefox_driver():
        # Замість Firefox використовуйте FirefoxOptions, якщо хочете додаткові налаштування
        driver = Firefox(executable_path="/шлях/до/geckodriver")
        return driver
