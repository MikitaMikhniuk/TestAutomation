
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def verify_current_page_title(self):
        current_page_title = self.driver.title()
        return current_page_title
    
    def verify_current_url(self):
        current_url = self.driver.current_url
        return current_url
