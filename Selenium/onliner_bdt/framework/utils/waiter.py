from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waiter(WebDriverWait):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    def wait_until_visibility_of_any_elements_located(self, element):
        self.wait.until(EC.visibility_of_any_elements_located(element))

    def wait_until_not_presence_of_element_located(self, element):
        self.wait.until_not(EC.presence_of_element_located(element))

