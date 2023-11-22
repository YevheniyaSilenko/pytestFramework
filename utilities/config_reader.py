import configparser
from constants import ROOT_PATH

_abs_path = f'{ROOT_PATH}/configs/app_config.ini'
_config = configparser.RawConfigParser()
_config.read(_abs_path)


class AppConfig:
    url = _config.get('app_data', 'url')
    account_page_url = _config.get('page_urls', 'account_page')
    clothing_page_url = _config.get('page_urls', 'clothing_page')
    new_arrivales_page_url = _config.get('page_urls', 'new_arrivales_page')
    main_page_url = _config.get('page_urls', 'main_page')
    login_page_url = _config.get('page_urls', 'login_page')
    login = _config.get('user_data', 'login')
    password = _config.get('user_data', 'password')
    browser_id = _config.get('browser_data', 'browser_id')

