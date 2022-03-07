from selenium.webdriver.common.by import By


class BasePage:
    """
    Base page class.

    Contains basic methods available for all Steam pages.
    """
    def __init__(self, driver):
        self.driver = driver

    HTML_HEAD_LOCATOR = '//html[@class=" responsive"]'

    def go_to(self, URL):
        """
        Simple method to navigae to any URL you want.

        Input-> URL (str). e.g. https://store.steampowered.com/
        """
        self.driver.get(URL)

    def get_current_page_title(self):
        """
        Returns current page title (str).
        """
        current_page_title = self.driver.title()
        return current_page_title

    def get_current_url(self):
        """
        Returns current page URL (str).
        """
        current_url = self.driver.current_url
        return current_url

    def get_current_language(self):
        """
        Returns current page lang (str) based on HTML <head>.
        Example: "en".
        """
        lang_element = self.driver.find_element(By.XPATH, self.HTML_HEAD_LOCATOR)
        current_lang = lang_element.get_attribute("lang")
        return current_lang

    def scroll_element_into_view(self, element):
        """
        Scrolls down to the input Selenium element.

        Input-> Element (selenium element).
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def verify_current_page_by_url(self, URL):
        """
        Assertion methond to compare current page URL with the given one (input).

        Input-> URL (str).
        """
        assert self.get_current_url() == URL

    def verify_current_page_by_title(self, title):
        """
        Assertion methond to compare current page title with the given one (input).

        Input-> title (str).
        """
        assert self.get_current_page_title() == title
