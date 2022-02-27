import pytest
from framework.utils.driver_factory import DriverFactory

@pytest.fixture
def setup():
    driver_instance = DriverFactory()
    driver = driver_instance.setUp()
    yield driver
    DriverFactory.tearDown(driver)