import pytest
import json
from framework.utils.driver_factory import DriverFactory
from framework.utils.browser import Browser


@pytest.fixture(scope="session")
def setup():
    driver_instance = DriverFactory()
    driver = driver_instance.set_up()
    yield driver
    Browser.tear_down(driver)
    
@pytest.fixture(scope="session")
def test_data():
    file = open("onliner\\resources\\test_data.json")
    data = json.load(file)
    yield data
