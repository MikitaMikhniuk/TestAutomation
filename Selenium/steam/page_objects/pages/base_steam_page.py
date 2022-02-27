from framework.base.base_page import BasePage


class BaseSteamPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SELECTED_APP_ID = None
    SELECTED_GENRE = None
    AGE_CHECK_BASE_URL = "https://store.steampowered.com/agecheck/app/"
    APP_BASE_URL = "https://store.steampowered.com/app/"
    BASE_STEAM_URL = "https://store.steampowered.com/"
