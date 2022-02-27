from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

from framework.base.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    DISCOUNTED_PRICES_LOCATOR = '//div[@class="contenthub_specials_grid"]//div[@class="discount_prices"]'
    DISCOUNTED_PERCENTAGES_LOCATOR = '//a[@class="store_capsule app_impression_tracked"]//div[@class="discount_pct"]'
    APPID_LOCATOR = '//a[@class="store_capsule app_impression_tracked"]'
    RECOMMENDED_SPECIALS_ID = 'specials_container'
    GAME_ITEM_LOCATOR = '//a[@class="store_capsule app_impression_tracked" and @data-ds-appid="GAME_ID"]'
    PAGEHEADER_LOCATOR = '//h2[@class="pageheader"]'

    def verify_category_page(self):
        category_header = self.driver.find_element(By.XPATH, self.PAGEHEADER_LOCATOR)
        category_header_text = (category_header.text).strip()
        return category_header_text

    def get_max_discount_recommended_special_item(self):
        tab = self.driver.find_element(By.ID, self.RECOMMENDED_SPECIALS_ID)
        self.scroll_element_into_view(tab)
        app_id_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.APPID_LOCATOR)))
        discount_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.DISCOUNTED_PERCENTAGES_LOCATOR)))
        app_ids = []
        discounts = []
        for id_element in app_id_elements:
            app_id = id_element.get_attribute("data-ds-appid")
            app_ids.append(app_id)
        for discount_element in discount_elements:
            discount = discount_element.text
            discounts.append(discount)
        res = dict(zip(app_ids, discounts))
        max_discount_ids = [key for key, value in res.items() if value == max(res.values())]  
        if len(max_discount_ids) > 1:
            game_id = random.choice(max_discount_ids)
            game_item_locator = self.GAME_ITEM_LOCATOR.replace("GAME_ID", game_id)
            element = self.driver.find_element(By.XPATH, game_item_locator)
            return element, game_id
        else:
            game_id = max_discount_ids[0]
            game_item_locator = self.GAME_ITEM_LOCATOR.replace("GAME_ID", game_id)
            element = self.driver.find_element(By.XPATH, game_item_locator)
            return element, game_id
    
    def click_on_max_discount_game(self):
        element, id = self.get_max_discount_recommended_special_item()
        element.click()
        return id