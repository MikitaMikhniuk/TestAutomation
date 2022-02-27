from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class AgeVerificationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    WARNING_LOCATOR = '//h2'
    AGE_DAY_SELECTOR_ID = 'ageDay'
    AGE_MONTH_SELECTOR_ID = 'ageMonth'
    AGE_YEAR_SELECTOR_ID = 'ageYear'
    VIEW_PAGE_BTN_ID = 'view_product_page_btn'
    AGE_CHECK_KEYWORD_ID = "/agecheck/"

    def set_user_dob(self, day="28", month= "August", year="1995"):
        day_selector = self.driver.find_element(By.ID, self.AGE_DAY_SELECTOR_ID)
        day_selector.click()
        Select(day_selector).select_by_value(day)
        month_selector = self.driver.find_element(By.ID, self.AGE_MONTH_SELECTOR_ID)
        month_selector.click()
        Select(month_selector).select_by_value(month)
        year_selector = self.driver.find_element(By.ID, self.AGE_YEAR_SELECTOR_ID)
        year_selector.click()
        Select(year_selector).select_by_value(year)
        
    def get_current_appid_from_url(self): # TODO
        url = self.get_current_url()
        app_id = url.replace("https://store.steampowered.com/app")
        print(app_id)
        return app_id

    def wait_for_age_verification_page(self):
        url = self.get_current_url()
        if self.AGE_CHECK_KEYWORD_ID in url:
            print("Age check!")
            self.set_user_dob()
            view_page_btn = self.driver.find_element(By.ID, self.VIEW_PAGE_BTN_ID)
            view_page_btn.click()
        else:
            print("No age check!")
            pass