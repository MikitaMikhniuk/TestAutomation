from page_objects.main_page import MainPage
from page_objects.catalog_page import CatalogPage
from page_objects.result_page import ResultPage
from framework.utils.browser import Browser


def test_onliner_tv_flow(setup, test_data):
    driver = setup
    browser = Browser(driver)
    browser.navigate(test_data["URL"])

    main_page = MainPage(driver)
    main_page.verify_main_page()
    main_page.click_on_catalog_top_bar("Каталог")

    catalog = CatalogPage(driver)
    catalog.verify_catalog_page_by_header("Каталог")
    catalog.navigate_to_menu("Электроника")
    catalog.navigate_to_submenu("Телевидение и видео")
    catalog.click_on_submenu_item("Телевизоры")

    results = ResultPage(driver)
    results.verify_result_page_by_header("Телевизоры")
    results.click_on_filter_checkbox(test_data["VENDOR"])
    results.set_max_price(test_data["MAX_PRICE"])
    results.click_on_filter_checkbox(test_data["RESOLUTION"])
    results.set_min_size(test_data["MIN_SIZE"])
    results.set_max_size(test_data["MAX_SIZE"])
    results.wait_for_filter_results()

    results.assert_headers(test_data["VENDOR"])
    results.assert_descriptions(
        test_data["RESOLUTION"], test_data["MIN_SIZE"], test_data["MAX_SIZE"])
    results.assert_prices(test_data["MAX_PRICE"])
