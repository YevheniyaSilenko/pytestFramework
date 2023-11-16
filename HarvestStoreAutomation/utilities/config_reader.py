import os
from configparser import ConfigParser

# Визначте шлях до конфігураційного файлу
CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configs', 'app_config.ini')

class AppConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_FILE_PATH)

    def get_app_url(self):
        return self.config.get('app_data', 'url')

    def get_page_url(self, page_name):
        return self.config.get('page_urls', page_name)

    def get_user_data(self):
        login = self.config.get('user_data', 'login')
        password = self.config.get('user_data', 'password')
        return login, password

    def get_browser_id(self):
        return self.config.get('browser_data', 'browser_id')


# Створимо екземпляр AppConfig, який можна буде використовувати в тестах
app_config = AppConfig()
