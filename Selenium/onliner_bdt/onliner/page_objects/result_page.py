from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from onliner_bdt.framework.base.base_page import BasePage
from onliner_bdt.framework.base.base_element import BaseElement

class ResultPage(BasePage, BaseElement):
    
    def __init__(self, driver):
        super().__init__(driver)

    FILTER_CHECKBOX = (By.XPATH, f'//span[@class="schema-filter__checkbox-text" and text()="keyword"]')
    LOADING_ANIM = (By.XPATH, '//div[@class="schema-products schema-products_processing"]')
    MIN_PRICE_INPUT = (By.XPATH, '//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="от"]')
    MAX_PRICE_INPUT = (By.XPATH, '//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="до"]')
    SCHEMA_PROD = (By.XPATH, '//div[@class="schema-products"]')
    MIN_SIZE_INPUT = (By.XPATH, '//select[contains(@class,"schema-filter-control__item")]')
    MIN_SIZE_VALUE_OPTION = (By.XPATH, f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]//option[@value="VALUE"]')
    MAX_SIZE_INPUT = (By.XPATH, '//div[contains(@class,"schema-filter-control schema-filter-control_select")]/following-sibling::div/select')
    MAX_SIZE_VALUE_OPTION = (By.XPATH, f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]/following-sibling::div/select//option[@value="VALUE"]')
    ITEM_HEADERS = (By.XPATH, '//span[contains(@data-bind,"html: product.extended_name || product.full_name")]')
    ITEM_DESCRIPTIONS = (By.XPATH, '//span[contains(@data-bind,"html: product.description")]')
    ITEM_PRICES = (By.XPATH, '//span[@data-bind="html: $root.format.minPrice($data.prices, ''BYN'')"]')
    RESULT_PAGE_TITLE = (By.XPATH, '//h1[contains(@class,"schema-header__title")]')



    def click_on_filter_checkbox(self, keyword):
        filter_checkbox = self.find_element(self.get_locator_with_replace(self.FILTER_CHECKBOX, "keyword", keyword))
        self.scroll_element_into_view(filter_checkbox)
        actions = ActionChains(self.driver)
        actions.move_to_element(filter_checkbox).click().perform()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        return filter_checkbox
    
    def set_min_price(self, min_price):
        min_price_input = self.find_element(self.MIN_PRICE_INPUT)
        actions = ActionChains(self.driver)
        actions.move_to_element(min_price_input) # TODO
        self.click_on_element(min_price_input)
        min_price_input.send_keys(min_price) # TODO
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        return min_price_input

    def set_max_price(self, max_price):
        max_price_input = self.find_element(self.MAX_PRICE_INPUT)
        actions = ActionChains(self.driver)
        actions.move_to_element(max_price_input)
        self.click_on_element(max_price_input)
        max_price_input.send_keys(max_price)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(self.SCHEMA_PROD))
        return max_price_input
    
    def set_min_size(self, value):
        min_size_input = self.find_element(self.MIN_SIZE_INPUT)
        self.click_on_element(min_size_input)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(self.get_locator_with_replace(self.MIN_SIZE_VALUE_OPTION, "VALUE", value)))
        Select(min_size_input).select_by_value(value)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        return min_size_input

    def set_max_size(self, value):
        max_size_input = self.find_element(self.MAX_SIZE_INPUT)
        self.click_on_element(max_size_input)
        Select(max_size_input).select_by_value(value)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(self.get_locator_with_replace(self.MAX_SIZE_VALUE_OPTION, "VALUE", value)))
        self.click_on_element(max_size_input)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        return max_size_input

    def find_item_headers(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        item_headers = self.find_elements(self.ITEM_HEADERS)
        return item_headers

    def find_item_descriptions(self):
        item_descriptions = self.find_elements(self.ITEM_DESCRIPTIONS)
        return item_descriptions

    def find_item_prices(self):
        item_prices = self.find_elements(self.ITEM_PRICES)
        return item_prices

    def verify_result_page(self):
        result_page_header = self.find_element(self.RESULT_PAGE_TITLE)
        wait = WebDriverWait(self.driver, 5)    
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))
        assert result_page_header.text == "Телевизоры"

    def wait_for_filter_results(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(EC.presence_of_element_located(self.LOADING_ANIM))

    def assert_headers(self, vendor):
        for item_header in self.find_item_headers():
            assert f"Телевизор {vendor}" in item_header.text
    
    def assert_descriptions(self, resolution, min_size, max_size):
        for item_description in self.find_item_descriptions():
            assert resolution in item_description.text
            description_list = item_description.text.split()
            size = description_list[0]
            assert (float(min_size))/10 <= float(size.replace('"', '')) <= (float(max_size))/10

    def assert_prices(self, max_price):
        for item_price in self.find_item_prices():
            price = item_price.text.replace('\u00A0р.', '')
            assert int(price) <= int(max_price) 