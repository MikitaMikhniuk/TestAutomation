import pytest
import json

CONFIG_PATH = "Selenium\\steam\\framework\\resources\\factory_config.json"


@pytest.fixture(scope="module")
def get_factory_config():
    config_file = open(CONFIG_PATH)
    factory_config = json.load(config_file)
    return factory_config
