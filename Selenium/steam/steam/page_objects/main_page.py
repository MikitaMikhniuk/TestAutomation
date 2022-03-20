from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class MainPage(BaseSteamPage):
    """
    Steam main page class.

    Contains methods for working with the main page objects.
    """

    def __init__(self, driver):
        super().__init__(driver)

    MENU_XPATH_LOCATOR = '//a[@class="pulldown_desktop" and text()="value"]'
    SUBMENU_XPATH_LOCATOR = '//a[@class="popup_menu_item" and translate(normalize-space(text()),"\u00A0"," ")="genre"]'
    TAB_XPATH_LABEL = '//span[text()="value"]'
    MODAL_TAB = '//div[@class="newmodal"]'

    # def get_menu_tab(self, value):
    #     """
    #     Method is used to get Menu tab element.

    #     Input-> Menu label (str). Example: "Categories".
    #     """
    #     element = self.MENU_XPATH_LOCATOR.replace("value", value)
    #     menu_tab = self.driver.find_element(By.XPATH, element)
    #     return menu_tab

    def get_seubmenu_item(self, genre):
        """
        Method is used to get Submenu tab element.

        Input-> Submenu label (str). Example: "Action".
        """
        submenu_item = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.SUBMENU_XPATH_LOCATOR, "genre", genre))
        self.SELECTED_GENRE = genre
        return submenu_item, genre

    def navigate_menu(self, menu_item_name, submenu_item_name):
        """
        Complex method for navigating through the Steam navigation menu.

        Input-> Menu label (str). Example: "Categories".
        Input-> Menu label (str). Example: "Action".
        """
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until_not(EC.visibility_of_element_located((By.XPATH, self.MODAL_TAB)))
        # menu_item = self.get_menu_tab(menu_item_name)
        menu_item = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.MENU_XPATH_LOCATOR, "value", menu_item_name))
        # menu_item.click()
        self.click_on_element(menu_item)
        submenu_item, genre = self.get_seubmenu_item(submenu_item_name)
        # submenu_item.click()
        self.click_on_element(submenu_item)
        return genre
