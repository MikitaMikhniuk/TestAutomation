from onliner.page_objects.main_page import MainPage
from onliner.page_objects.catalog_page import CatalogPage
from onliner.page_objects.result_page import ResultPage
from behave import *


@given(u'website "{url}"')
def step_impl(context, url):
    context.browser.navigate(url)


@when(u'main page is opened')
def step_impl(context):
    context.main_page = MainPage(context.driver)
    context.main_page.verify_main_page()


@then(u'click top bar "{section}" button')
def step_impl(context, section):
    context.main_page.click_on_catalog_top_bar(section)


@then(u'verify that main page is "{header}"')
def step_imp(context, header):
    context.catalog_page = CatalogPage(context.driver)
    context.catalog_page.verify_catalog_page_by_header(header)


@when(u'"{header}" page is opened')
def step_impl(context, header):
    context.catalog_page = CatalogPage(context.driver)
    context.catalog_page.verify_catalog_page_by_header(header)


@then(u'navigate to "{menu}" -> "{submenu}" -> "{item}"')
def step_imp(context, menu, submenu, item):
    context.catalog_page.navigate_to_menu(menu)
    context.catalog_page.navigate_to_submenu(submenu)
    context.catalog_page.click_on_submenu_item(item)


@then(u'verify that page is "{section}"')
def step_impl(context, section):
    context.result_page = ResultPage(context.driver)
    context.result_page.verify_result_page_by_header(section)


@when(u'current page is "{header}"')
def step_impl(context, section):
    context.result_page = ResultPage(context.driver)
    context.result_page.verify_result_page_by_header(section)


@then(u'click on "{filter}" filter')
def step_impl(context, filter):
    context.results.click_on_filter_checkbox(filter)


@then(u'set max price to "{price}"')
def step_impl(context, price):
    context.results.set_max_price(price)


@then(u'set size range between "{min_size}" and "{max_size}"')
def step_impl(context, min_size, max_size):
    context.results.set_min_size(min_size)
    context.results.set_max_size(max_size)


@then(u'set resolution to "{resolution}"')
def step_impl(context, resolution):
    context.results.click_on_filter_checkbox(resolution)


@then(u'assert filter results')
def step_impl(context):
    context.results.wait_for_filter_results()
    context.results.assert_headers(test_data["VENDOR"])
    context.results.assert_descriptions(
        test_data["RESOLUTION"], test_data["MIN_SIZE"], test_data["MAX_SIZE"])
    context.results.assert_prices(test_data["MAX_PRICE"])
