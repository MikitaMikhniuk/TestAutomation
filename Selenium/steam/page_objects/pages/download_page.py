from framework.utils.downloader import wait_for_download_finish
from page_objects.pages.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class DownloadPage(BaseSteamPage):
    """
    Downlaod page class.

    Contains methods for working with the Steam download page (about).
    """

    def __init__(self, driver):
        super().__init__(driver)

    INSTALL_BUTTON_XPATH = '//a[@class="about_install_steam_link"]'

    def download_installer(self):
        """
        Method is used to click on "Download Steam" button.
        And wait for download finish.
        """
        install_button = self.driver.find_element(
            By.XPATH, self.INSTALL_BUTTON_XPATH)
        install_button.click()
        wait_for_download_finish("SteamSetup.exe")
