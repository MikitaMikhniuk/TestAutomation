from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
import json

class DriverSetUp:

    def setUp(self):
        file = open("resources\config.json")
        data = json.load(file)
        if data["BROWSER"] == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        elif data["BROWSER"] == "Firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return driver
        elif data["BROWSER"] == "Edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            return driver
        else:
            print("Sorry! I don't know such driver yet!")

    def goTo(self, driver):
        file    = open("resources\config.json")
        data = json.load(file)
        driver.maximize_window()
        driver.get(data["URL"])
        # return driver

    def tearDown(self, driver):
        if (driver != None):
            print("Cleanup of test environment")
            driver.close()
            driver.quit()

driverSetUp = DriverSetUp()