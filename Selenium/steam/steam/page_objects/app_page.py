from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AppPage(BaseSteamPage):
    """
    App page class.

    Contains methond for working with application page.
    """

    def __init__(self, driver):
        super().__init__(driver)

    INSTALL_BTN_XPATH = '//a[@class="header_installsteam_btn_content"]'
    APP_NAME_ID = "appHubAppName"

    def verify_curent_app_page(self, app_id):
        """
        Assertion methond to compare current page app id with the given one (input).

        Input-> app id (str).
        """
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, self.APP_NAME_ID)))
        id = self.get_current_appid_from_url()
        assert id == app_id

    def go_to_download_page(self):
        """
        Help method is used to click on Global header download button.
        """
        btn = self.driver.find_element(By.XPATH, self.INSTALL_BTN_XPATH)
        btn.click()
