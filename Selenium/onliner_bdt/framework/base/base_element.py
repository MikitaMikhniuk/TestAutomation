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
