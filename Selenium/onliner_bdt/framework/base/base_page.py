from selenium.webdriver.common.by import By


class BasePage:
    """
    Base page class.

    Contains basic methods available for all pages.
    """
    def __init__(self, driver):
        self.driver = driver

    HTML_HEAD_LOCATOR = (By.XPATH, '//html[@class=" responsive"]')

    def navigate(self, url):
        """
        Simple method to navigae to any URL you want.

        Input-> URL (str).
        """
        self.driver.get(url)

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
        lang_element = self.driver.find_element(self.HTML_HEAD_LOCATOR)
        current_lang = lang_element.get_attribute("lang")
        return current_lang

    def get_locator_with_replace_xpath(self, input_xpath, replace_what, replace_to):
        """
        Method for getting a locator with a replaced str.

        Input xpath - str
        
        Replace what (str) - a str to be replaced.

        Replace to (str) - a str to be inserted.

        Returns an element locator (tuple).
        """
        locator_xpath = input_xpath.replace(replace_what, replace_to)
        return locator_xpath

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
