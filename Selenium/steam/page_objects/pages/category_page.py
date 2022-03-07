import random
from framework.utils.lang_utils import get_label
from page_objects.pages.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CategoryPage(BaseSteamPage):
    """
    Steam Category page class.

    Contains methods for working with Category page elements.
    """

    def __init__(self, driver):
        super().__init__(driver)

    PAGEHEADER_LOCATOR = '//div[@class="contenthubmaincarousel_ContentHubTitle_saHqN"]'
    PAGEHEADER_ID = 'SaleSection_56339'
    SPECIALS_SECTION_LOCATOR = '//div[@class="saleitembrowser_FlavorLabel_KDLAS Focusable" and text()="TAB"]'
    DISCOUNTED_PERCENTAGES_LOCATOR = '//div[@class="facetedbrowse_FacetedBrowseInnerCtn_3vjDu"]//div[@class="salepreviewwidgets_StoreSaleDiscountBox_cnkoF"]'
    APP_NAMES_LOCATOR = '//div[@class="salepreviewwidgets_StoreSaleWidgetTitle_2ekpT"]'
    APP_LOCATOR = '//div[@class="salepreviewwidgets_TitleCtn_3rrH9"]/a[contains(@href, "APP_ID")]'
    RECOMMENDED_SPECIALS_ID = 'SaleSection_13268'
    APPID_LOCATOR = '//div[@class="salepreviewwidgets_TitleCtn_3rrH9"]//a'
    CONTENT_LOCATOR = '//div[@class="facetedbrowse_FacetedBrowseItems_3EdZT"]'
    GAME_ITEM = '//div[@class="salepreviewwidgets_SaleItemBrowserRow_gASJ2"]'
    

    def get_discount_locator(self):
        """
        Method is used to get Discount tab locator.

        Returns -> Discount tab XPATH locator
        """
        discount_locator = self.SPECIALS_SECTION_LOCATOR.replace(
            "TAB", get_label(self.driver, "Discounted"))
        return discount_locator

    def verify_category_page(self, genre):
        """
        Assertion methond to that currnet page is <input> page.

        Input-> Genre (str). e.g. "Action".
        """
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, self.PAGEHEADER_ID)))
        category_header = self.driver.find_element(
            By.XPATH, self.PAGEHEADER_LOCATOR)
        category_header_text = (category_header.text).strip()
        assert category_header_text == genre
        return category_header_text

    def get_max_discount_recommended_special_item(self):
        """
        Method is used to find the app with the max discount.

        Returns -> Max discount app element (Selenium element).
        Returns -> Max discount app id (str).
        """
        tab = self.driver.find_element(By.ID, self.RECOMMENDED_SPECIALS_ID)
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(EC.visibility_of(tab))
        discounted_btn = self.driver.find_element(
            By.XPATH, self.get_discount_locator())
        self.driver.execute_script("arguments[0].click();", discounted_btn)
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_any_elements_located((By.XPATH, self.GAME_ITEM)))
        discount_elements = self.driver.find_elements(
            By.XPATH, self.DISCOUNTED_PERCENTAGES_LOCATOR)
        app_id_elements = self.driver.find_elements(
            By.XPATH, self.APPID_LOCATOR)
        discounts = []
        app_ids = []
        for app_id_element in app_id_elements:
            app_link = app_id_element.get_attribute("href")
            app_id = self.get_current_appid_from_link(app_link)
            app_ids.append(app_id)
        for discount_element in discount_elements:
            discount = discount_element.text
            discounts.append(discount)
        res = dict(zip(app_ids, discounts))
        max_discount_ids = [key for key,
                            value in res.items() if value == max(res.values())]
        if len(max_discount_ids) > 1:
            app_id = random.choice(max_discount_ids)
        else:
            app_id = max_discount_ids[0]
        app_locator = self.APP_LOCATOR.replace("APP_ID", app_id)
        element = self.driver.find_element(By.XPATH, app_locator)
        return element, app_id

    def click_on_max_discount_game(self):
        """
        A complex method is used to find the app with the max discount
        and ckick on it.

        Retruns -> Max discount app id (str).
        """
        element, app_id = self.get_max_discount_recommended_special_item()
        action = ActionChains(self.driver)
        action.move_to_element(element)
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return app_id
