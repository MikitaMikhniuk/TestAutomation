from selenium.webdriver.common.by import By
from framework.base.base_page import BasePage
from framework.base.base_element import BaseElement


class MainPage(BasePage, BaseElement):

    def __init__(self, driver):
        super().__init__(driver)

    CATALOG_TOP_BAR = '//a[contains(@class,"b-main-navigation__link")]/span[text()="section"]'
    CATALOG_PAGE_SECTION = '//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(), normalize-space("section"))]'

    def click_on_catalog_top_bar(self, section):
        catalog_top_bar = self.find_element_by_xpath(self.get_locator_with_replace_xpath(self.CATALOG_TOP_BAR, "section", section))
        self.click_on_element(catalog_top_bar)
        return catalog_top_bar

    def click_on_catalog_page_section(self, section):
        catalog_page_section = self.find_element_by_xpath(self.get_locator_with_replace_xpath(self.CATALOG_PAGE_SECTION, "section", section))
        self.click_on_element(catalog_page_section)
        return catalog_page_section
