from framework.base.base_element import BaseElement
from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import json
from framework.utils.browser import Browser

CONFIG_PATH = "framework\\resources\\factory_config.json"

class BaseSteamPage(BasePage, BaseElement):
    """
    Base Steam page class.

    Contains basic methods available for all Steam pages.

    """
    def __init__(self, driver):
        super().__init__(driver)

    DEFAULT_WAIT_TIME = 5
    SELECTED_APP_ID = None
    SELECTED_GENRE = None
    AGE_CHECK_BASE_URL = "https://store.steampowered.com/agecheck/app/"
    APP_BASE_URL = "https://store.steampowered.com/app/"
    BASE_STEAM_URL = "https://store.steampowered.com/"
    LANG_DROPDOWN_ID = "language_pulldown"
 
    def get_current_appid_from_url(self):
        """
        Methond is used to get app id of the current app page URL.

        Returns -> app id (str).
        """
        browser = Browser(self.driver)
        url = browser.get_current_url()
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id = url_splitted[app_index+1]
        return app_id

    def get_current_appid_from_link(self, url):
        """
        Methond is used to get app id from any link.

        Input -> URL (str).

        Returns -> app id (str).
        """
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id_raw = url_splitted[app_index+1]
        app_id_splitted = app_id_raw.split("?")
        app_id = app_id_splitted[0]
        return app_id

    def get_lang_locator(self, lang):
        """
        Methond is used to generate a lang locator.

        Input -> Lang (str). Example: "russian", "english"

        Returns -> Lang Locator (str).
        """
        part = f"ChangeLanguage( '{lang}' )"
        part_x = f'"{part}"'
        lang_locator = f"//a[contains(@onclick, {part_x})]"
        return lang_locator
    
    def change_lang_to(self, lang):
        """
        Complex methond is used to change language on the page.

        Input -> Lang (str). Example: "russian", "english"
        """
        # lang_drop = self.driver.find_element(By.ID, self.LANG_DROPDOWN_ID)
        lang_drop = self.find_element_by_id(self.LANG_DROPDOWN_ID)
        # lang_drop.click()
        self.click_on_element(lang_drop)
        lang_locator = self.get_lang_locator(lang)
        # lang_btn = self.driver.find_element(By.XPATH, lang_locator)
        lang_btn = self.find_element_by_xpath(lang_locator)
        # lang_btn.click()
        self.click_on_element(lang_btn)

    
    def check_for_current_lang(self, desired_lang_code, desired_lang_full):
        """
        Complex methond is used to check language on the page.

        Input -> Desired Lang code (str). Example: "en", "ru".
        Input -> Desired Lang full (str). Example: "english", "russian".
        """
        if self.get_current_language() != desired_lang_code:
            self.change_lang_to(desired_lang_full)
            time.sleep(5)
        else:
            pass
    
    def get_factory_config(self):
        config_file = open(CONFIG_PATH)
        factory_config = json.load(config_file)
        BaseSteamPage.DEFAULT_WAIT_TIME = factory_config["DEFAULT_WAIT_TIME"]
        return factory_config
