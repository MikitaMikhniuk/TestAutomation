class BaseElement:
    """
    Base element class.

    Contains basic methods for working with elements.
    """
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(locator)
        return element
    
    def find_elements(self, locator):
        elements = self.driver.find_element(locator)
        return elements
    
    def click_on_element(self, element):
        element.click()

    def scroll_element_into_view(self, element):
        """
        Scrolls down to the input Selenium element.

        Input-> Element (selenium element).
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)