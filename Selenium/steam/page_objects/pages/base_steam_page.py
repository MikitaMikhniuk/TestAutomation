from framework.base.base_page import BasePage


class BaseSteamPage(BasePage):
    """
    Base Steam page class.

    Contains basic methods available for all Steam pages.

    """

    def __init__(self, driver):
        super().__init__(driver)

    SELECTED_APP_ID = None
    SELECTED_GENRE = None
    AGE_CHECK_BASE_URL = "https://store.steampowered.com/agecheck/app/"
    APP_BASE_URL = "https://store.steampowered.com/app/"
    BASE_STEAM_URL = "https://store.steampowered.com/"

    def get_current_appid_from_url(self):
        """
        Methond is used to get app id of the current app page URL.

        Returns -> app id (str).
        """
        url = self.get_current_url()
        print(url)
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id = url_splitted[app_index+1]
        return app_id

    def get_current_appid_from_link(self, url):
        """
        Methond is used to get app id from any link.

        Input -> URL (str).

        Returns -> app id (str).
        """
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id_raw = url_splitted[app_index+1]
        app_id_splitted = app_id_raw.split("?")
        app_id = app_id_splitted[0]
        return app_id
