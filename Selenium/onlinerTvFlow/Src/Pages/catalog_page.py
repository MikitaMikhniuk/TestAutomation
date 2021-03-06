from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage():

    def __init__(self, driver):
        self.driver = driver

    def click_on_nav_classifier(self, section):
        nav_classifier = self.driver.find_element(By.XPATH, f'//span[contains(@class,"catalog-navigation-classifier__item-title-wrapper") and translate(text(),"\u00A0"," ")="{section}"]')
        nav_classifier.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="catalog-navigation-list__aside-list"]')))
        return nav_classifier
    
    def click_on_nav_subclass(self, section):
        nav_subclass = self.driver.find_element(By.XPATH, f'//div[contains(@class,"catalog-navigation-list__aside-title") and translate(normalize-space(text()),"\u00A0"," ")="{section}"]')
        nav_subclass.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="catalog-navigation-list__dropdown"]')))
        return nav_subclass
    
    def click_on_aside_item(self, section):
        aside_item = self.driver.find_element(By.XPATH, f'//span[contains(@class,"catalog-navigation-list__dropdown-title") and translate(normalize-space(text()),"\u00A0"," ")="{section}"]')
        aside_item.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        return aside_item

    def verify_catalog_page(self):
        catalog_header_whole = self.driver.find_element(By.XPATH, '//div[@class="catalog-navigation__title"]')
        catalog_super_price = self.driver.find_element(By.XPATH, '//div[@class="catalog-navigation__title"]//a')
        catalog_header = catalog_header_whole.text.replace(catalog_super_price.text, '')
        assert catalog_header == "Каталог"
        return catalog_header