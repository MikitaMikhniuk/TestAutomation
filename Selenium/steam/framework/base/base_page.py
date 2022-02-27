from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    HTML_HEAD_LOCATOR = (By.XPATH, '//html[@class=" responsive"]')

    def go_to(self):
        self.driver.get()

    def get_current_page_title(self):
        current_page_title = self.driver.title()
        return current_page_title
    
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_current_language(self):
        lang_element = self.driver.find_elemet(self.HTML_HEAD_LOCATOR)
        current_lang = lang_element.get_attribute("lang")
        return current_lang

    def scroll_element_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def verify_current_page_by_url(self, URL):
        assert self.get_current_url() == URL
    
    def verify_current_page_by_title(self, title):
        assert self.get_current_page_title() == title