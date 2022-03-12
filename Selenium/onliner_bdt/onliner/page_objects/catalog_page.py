from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from onliner_bdt.framework.base.base_page import BasePage
from onliner_bdt.framework.base.base_element import BaseElement

class CatalogPage(BasePage, BaseElement):

    def __init__(self, driver):
        super().__init__(driver)

    NAV_CLASS = (By.XPATH, f'//span[contains(@class,"catalog-navigation-classifier__item-title-wrapper") and translate(text(),"\u00A0"," ")="section"]')
    ASIDE_LIST = (By.XPATH, '//div[@class="catalog-navigation-list__aside-list"]')
    NAV_SUBCLASS = (By.XPATH, f'//div[contains(@class,"catalog-navigation-list__aside-title") and translate(normalize-space(text()),"\u00A0"," ")="section"]')
    NAV_LIST = (By.XPATH, '//div[@class="catalog-navigation-list__dropdown"]')
    ASIDE_ITEM = (By.XPATH, f'//span[contains(@class,"catalog-navigation-list__dropdown-title") and translate(normalize-space(text()),"\u00A0"," ")="section"]')
    LOADING_BAR = (By.XPATH, '//div[@class="schema-products schema-products_processing"]')
    CATALOG_HEADER_FULL = (By.XPATH, '//div[@class="catalog-navigation__title"]')
    CATALOG_HEADER_SUPERPRICE = (By.XPATH, '//div[@class="catalog-navigation__title"]//a')

    def click_on_nav_class(self, section):
        nav_class = self.find_element(self.get_locator_with_replace(self.NAV_CLASS, "section", section))
        self.click_on_element(nav_class)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_any_elements_located(self.ASIDE_LIST))
        return nav_class

    def click_on_nav_subclass(self, section):
        nav_subclass = self.find_element(self.get_locator_with_replace(self.NAV_SUBCLASS, "section", section))
        self.click_on_element(nav_subclass)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_any_elements_located(self.NAV_LIST))
        return nav_subclass

    def click_on_aside_item(self, section):
        aside_item = self.find_element(self.get_locator_with_replace(self.ASIDE_ITEM, "section", section))
        self.click_on_element(aside_item)
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located(self.LOADING_BAR))
        return aside_item

    def verify_catalog_page(self):
        catalog_header_whole = self.find_element(self.CATALOG_HEADER_FULL)
        catalog_super_price = self.find_element(self.CATALOG_HEADER_SUPERPRICE)
        catalog_header = catalog_header_whole.text.replace(catalog_super_price.text, '')
        assert catalog_header == "Каталог"
        return catalog_header
