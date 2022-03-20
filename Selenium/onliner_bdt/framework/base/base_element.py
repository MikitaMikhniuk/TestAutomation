from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement:
    """
    Base element class.

    Contains basic methods for working with elements.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def find_element_by_xpath(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def find_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return elements
    
    def click_on_element(self, element):
        element.click()

    def scroll_element_into_view(self, element):
        """
        Scrolls down to the input Selenium element.

        Input-> Element (selenium element).
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def apply_style_to_element(self, element, style):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, style)
    
    def get_original_style(self, element):
        orignal_style = element.get_attribute('style')
        return orignal_style

    def click_on_element_with_highlight(self, element, style= "border: 4px solid red"):
        original_style = self.get_original_style(element)
        self.apply_style_to_element(element, style)
        element.click()
        self.apply_style_to_element(element, original_style)

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

    def send_keys(self, element, keys):
        element.send_keys(keys)

    def select_by_dropdown_value(self, element, value):
        Select(element).select_by_value(value)

    def wait_for_visibility_of_any_elements_located(self, elements):
        pass

    def wait_for_presence_of_element_located(self, element):
        pass

    def wait_for_visibility_of_element_located(self, element):
        pass
