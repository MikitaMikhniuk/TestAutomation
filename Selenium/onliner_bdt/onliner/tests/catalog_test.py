from page_objects.main_page import MainPage
from page_objects.catalog_page import CatalogPage
from page_objects.result_page import ResultPage
import pytest
import json
from framework.utils.navigation import navigate_to

@pytest.fixture
def test_data():
    file = open("onliner\\resources\\test_data.json")
    data = json.load(file)
    yield data

def test_onliner_tv_flow(setup, test_data):
    driver = setup
    vendor = test_data["VENDOR"]
    max_price = test_data["MAX_PRICE"]
    min_size = test_data["MIN_SIZE"]
    max_size = test_data["MAX_SIZE"]
    resolution = test_data["RESOLUTION"]
    landing_url = test_data["LANDING_URL"]
    
    navigate_to(driver, landing_url)

    landing = MainPage(driver)
    landing.click_on_catalog_top_bar("Каталог")

    catalog = CatalogPage(driver)
    catalog.verify_catalog_page()
    catalog.click_on_nav_class("Электроника")
    catalog.click_on_nav_subclass("Телевидение и видео")
    catalog.click_on_aside_item("Телевизоры")

    results = ResultPage(driver)
    results.verify_result_page()
    results.click_on_filter_checkbox(vendor)
    results.set_max_price(max_price)
    results.click_on_filter_checkbox(resolution)
    results.set_min_size(min_size)
    results.set_max_size(max_size)
    results.wait_for_filter_results()

    results.assert_headers(vendor)
    results.assert_descriptions(resolution, min_size, max_size)
    results.assert_prices(max_price)
    
