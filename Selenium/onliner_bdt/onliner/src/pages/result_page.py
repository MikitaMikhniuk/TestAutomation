from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class ResultPage():
    
    def __init__(self, driver):
        self.driver = driver

    def click_on_filter_checkbox(self, keyword):
        filter_checkbox = self.driver.find_element(By.XPATH, f'//span[@class="schema-filter__checkbox-text" and text()="{keyword}"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_checkbox)
        actions = ActionChains(self.driver)
        actions.move_to_element(filter_checkbox).click().perform()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        return filter_checkbox
    
    def set_min_price(self, min_price):
        min_price_input = self.driver.find_element(By.XPATH, '//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="от"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(min_price_input)
        min_price_input.click()
        min_price_input.send_keys(min_price)
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        return min_price_input

    def set_max_price(self, max_price):
        max_price_input = self.driver.find_element(By.XPATH, '//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="до"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(max_price_input)
        max_price_input.click()
        max_price_input.send_keys(max_price)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products"]')))
        return max_price_input
    
    def set_min_size(self, value):
        min_size_input = self.driver.find_element(By.XPATH, '//select[contains(@class,"schema-filter-control__item")]')
        min_size_input.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]//option[@value="{value}"]')))
        Select(min_size_input).select_by_value(value)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        return min_size_input

    def set_max_size(self, value):
        max_size_input = self.driver.find_element(By.XPATH, '//div[contains(@class,"schema-filter-control schema-filter-control_select")]/following-sibling::div/select')
        max_size_input.click()
        Select(max_size_input).select_by_value(value)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]/following-sibling::div/select//option[@value="{value}"]')))
        max_size_input.click()
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        return max_size_input

    def find_item_headers(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        item_headers = self.driver.find_elements(By.XPATH, '//span[contains(@data-bind,"html: product.extended_name || product.full_name")]')
        return item_headers

    def find_item_descriptions(self):
        item_descriptions = self.driver.find_elements(By.XPATH, '//span[contains(@data-bind,"html: product.description")]')
        return item_descriptions

    def find_item_prices(self):
        item_prices = self.driver.find_elements(By.XPATH, '//span[@data-bind="html: $root.format.minPrice($data.prices, ''BYN'')"]')
        return item_prices

    def verify_result_page(self):
        result_page_header = self.driver.find_element(By.XPATH, '//h1[contains(@class,"schema-header__title")]')
        wait = WebDriverWait(self.driver, 5)    
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))
        assert result_page_header.text == "Телевизоры"

    def wait_for_filter_results(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="schema-products schema-products_processing"]')))

    def scroll_a_litlle_bit(self, multiplier=1):
        page = self.driver.find_element(By.XPATH, '//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="от"]')
        page.send_keys('\ue00f' *multiplier)