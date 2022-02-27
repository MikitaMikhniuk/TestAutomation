
from page_objects.pages.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class AppPage(BaseSteamPage):
    def __init__(self, driver):
        super().__init__(driver)

    COMMUNITY_BUTTON_XPATH = '//div[@class="apphub_OtherSiteInfo"]/a'
    
    def get_current_appid_from_community(self):
        game_community_button = self.driver.find_element(By.XPATH, self.COMMUNITY_BUTTON_XPATH)
        game_community_href = game_community_button.get_attribute("href")
        id = game_community_href.repalce(self.AGE_CHECK_BASE_URL, "")
        app_id = id.replace("/", "")
        return app_id

    def verify_curent_app_page(self):
        app_id = self.get_current_appid_from_community()
        assert app_id == self.SELECTED_APP_ID