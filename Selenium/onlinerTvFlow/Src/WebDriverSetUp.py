from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium import webdriver
import json

class WebDriverSetUp:

    def SetUp(self):
        file = open("Selenium\onlinerTvFlow\Resources\config.json")
        data = json.load(file)
        if data["driver_config"]["BROWSER"] == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        elif data["driver_config"]["BROWSER"] == "Firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return driver
        elif data["driver_config"]["BROWSER"] == "Edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            return driver
        else:
            print("Sorry! I don't know such driver yet!")
        
    def TearDown(self, driver):
        if (driver != None):
            print("Cleanup of test environment")
            driver.close()
            driver.quit()

# a = WebDriverSetUp()
# driver = a.SetUp()
# # print(driver)
# a.TearDown(driver)