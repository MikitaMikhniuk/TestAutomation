from selenium.webdriver.common import actions
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select

class Actions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()
    
    def move_to_element(self, element):
        move_to_element(element)
        