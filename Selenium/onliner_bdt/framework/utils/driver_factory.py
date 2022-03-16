from selenium import webdriver
import json
from framework.utils.browser import Browser

CONFIG_PATH = "framework\\resources\\factory_config.json"

class DriverFactory:
    """
    Creates a webdriver instance based on factory_config.json

    """
    @staticmethod
    def set_up():
        """
        Driver set up.
        """
        config_file = open(CONFIG_PATH)
        factory_config = json.load(config_file)
        s, options = Browser.browser_setup()
        if factory_config["BROWSER"] == "Chrome":
            driver = webdriver.Chrome(service=s, options=options)
        elif factory_config["BROWSER"] == "Firefox":
            driver = webdriver.Firefox(service=s, options=options)
        else:
            raise Exception("I don't know such driver yet!")
        return driver
