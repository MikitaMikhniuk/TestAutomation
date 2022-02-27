from selenium.webdriver.common.by import By
from page_objects.pages.base_steam_page import BaseSteamPage


class MainPage(BaseSteamPage):

    def __init__(self, driver):
        super().__init__(driver)

    MENU_XPATH_LOCATOR = '//a[@class="pulldown_desktop" and text()="value"]'
    SUBMENU_XPATH_LOCATOR = '//a[@class="popup_menu_item" and translate(normalize-space(text()),"\u00A0"," ")="genre"]'
    TAB_XPATH_LABEL = '//span[text()="value"]'

    def get_menu_tab(self, value):
        element = self.MENU_XPATH_LOCATOR.replace("value", value)
        menu_tab = self.driver.find_element(By.XPATH, element)
        return menu_tab

    def get_seubmenu_item(self, genre):
        element = self.SUBMENU_XPATH_LOCATOR.replace("genre", genre)
        submenu_item = self.driver.find_element(By.XPATH, element)
        self.SELECTED_GENRE = genre
        return submenu_item, genre

    def navigate_menu(self, menu_item_name, submenu_item_name):
        menu_item = self.get_menu_tab(menu_item_name)
        menu_item.click()
        # add wait
        submenu_item, genre = self.get_seubmenu_item(submenu_item_name)
        submenu_item.click()
        return genre

    def click_download(self):
        element = self.driver.find_element(
            By.XPATH, "//a[@class='about_install_steam_link']")
        element.click()
