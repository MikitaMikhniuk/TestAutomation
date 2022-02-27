from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service
import os

CONFIG_PATH = "Selenium\\steam\\framework\\resources\\factory_config.json"


class DriverFactory:
    """
    Creates a webdriver instance based on factory_config.json

    """

    @staticmethod
    def setUp():
        config_file = open(CONFIG_PATH)
        factory_config = json.load(config_file)

        default_download_path = os.path.join(os.getcwd(), factory_config["DEFAULT_DOWNLOAD_PATH"])
        if factory_config["BROWSER"] == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--safebrowsing-disable-download-protection")

            file_prefs = {"download.default_directory": default_download_path,
                          "download.prompt_for_download": False,
                          "safebrowsing.enabled": True}
            options.add_experimental_option("prefs", file_prefs)
            if factory_config["HEADLESS_MODE"] is True:
                options.add_argument("--headless")
            s = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s, options=options)
            return driver
        elif factory_config["BROWSER"] == "Firefox":
            options = webdriver.FirefoxOptions()
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference(
                "browser.download.manager.showWhenStarting", False)
            profile.set_preference(
                "browser.download.dir", factory_config["DEFAULT_DOWNLOAD_PATH"])
            profile.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            if factory_config["HEADLESS_MODE"] is True:
                options.headless = True
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(), firefox_profile=profile, options=options)
            return driver
        else:
            raise Exception("I don't know such driver yet!")

    @staticmethod
    def tearDown(driver):
        if (driver != None):
            print("Cleanup of test environment!")
            driver.close()
            driver.quit()
