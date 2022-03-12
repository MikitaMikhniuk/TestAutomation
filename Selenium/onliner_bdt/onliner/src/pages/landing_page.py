from selenium.webdriver.common.by import By

class LandingPage():
            
    def __init__(self, driver):
        self.driver = driver

    def click_on_catalog_top_bar(self, section):
        catalog_top_bar = self.driver.find_element(By.XPATH, f'//a[contains(@class,"b-main-navigation__link")]/span[text()="{section}"]')
        catalog_top_bar.click()
        return catalog_top_bar

    def click_on_catalog_page_section(self, section):
        catalog_page_section = self.driver.find_element(By.XPATH, f'//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(), normalize-space("{section}"))]')
        catalog_page_section.click()
        return catalog_page_section

    def verify_landing_page(self, landing_url):
        current_url = self.driver.current_url
        assert current_url == landing_url
        return current_url