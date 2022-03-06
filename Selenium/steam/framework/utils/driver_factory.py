from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxSerive
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.utils.downloader import set_up_download_folder

CONFIG_PATH = "Selenium\\steam\\framework\\resources\\factory_config.json"


class DriverFactory:
    """
    Creates a webdriver instance based on factory_config.json

    """

    @staticmethod
    def setUp():
        """
        Driver set up.
        """
        config_file = open(CONFIG_PATH)
        factory_config = json.load(config_file)
        default_download_path = set_up_download_folder(factory_config)
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
            s = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s, options=options)
            return driver
        elif factory_config["BROWSER"] == "Firefox":
            options = FirefoxOptions()
            # profile = webdriver.FirefoxProfile()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference(
                "browser.download.dir", default_download_path)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference(
                "browser.download.viewableInternally.enabledTypes", "")
            options.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            options.set_preference(
                "browser.download.manager.showWhenStarting", False)
            if factory_config["HEADLESS_MODE"] is True:
                options.headless = True
            s = FirefoxSerive(GeckoDriverManager().install())
            driver = webdriver.Firefox(
                service=s, options=options)
            return driver
        else:
            raise Exception("I don't know such driver yet!")

    @staticmethod
    def tearDown(driver):
        """
        Driver tear down.

        """
        if (driver != None):
            print("Cleanup of test environment!")
            driver.close()
            driver.quit()
