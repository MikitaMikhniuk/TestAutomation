from pages.conftest import driverSetUp
from pages.landing_page import LandingPage
from pages.catalog_page import CatalogPage
from pages.result_page import ResultPage
from selenium.common.exceptions import StaleElementReferenceException
import pytest
import json
import time

@pytest.fixture
def setup():
    driver = driverSetUp.setUp()
    yield driver
    driverSetUp.tearDown(driver)

@pytest.fixture
def test_data():
    file = open("tests\\test_data.json")
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

    driverSetUp.goTo(driver)

    landing = LandingPage(driver)
    landing.verify_landing_page(landing_url)
    landing.click_on_catalog_top_bar("Каталог")

    catalog = CatalogPage(driver)
    catalog.verify_catalog_page()
    catalog.click_on_nav_classifier("Электроника")
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
    

    for item_header in results.find_item_headers():
        assert f"Телевизор {vendor}" in item_header.text

    for item_description in results.find_item_descriptions():
        assert resolution in item_description.text
        description_list = item_description.text.split()
        size = description_list[0]
        assert (float(min_size))/10 <= float(size.replace('"', '')) <= (float(max_size))/10

    for item_price in results.find_item_prices():
        price = item_price.text.replace('\u00A0р.', '')
        assert int(price) <= int(max_price) 

# def stale_decorator(function):
#     try:
#         function()
#     except StaleElementReferenceException:
#         function()