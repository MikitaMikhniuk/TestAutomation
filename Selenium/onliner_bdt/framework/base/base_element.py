from selenium.webdriver.common.by import By

class BaseElement:
    """
    Base element class.

    Contains basic methods for working with elements.
    """
    def __init__(self, driver):
        self.driver = driver

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