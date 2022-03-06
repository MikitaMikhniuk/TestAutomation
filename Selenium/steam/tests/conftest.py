import os
import pytest
import json
from framework.utils.driver_factory import DriverFactory

CONFIG_PATH = "Selenium\\steam\\resources\\test_data.json"

@pytest.fixture
def setup():
    driver_instance = DriverFactory()
    driver = driver_instance.setUp()
    yield driver
    DriverFactory.tearDown(driver)
    
@pytest.fixture
def get_test_data():
    os.chdir("../../../../..")
    test_data_file = open(CONFIG_PATH)
    test_data = json.load(test_data_file)
    return test_data
