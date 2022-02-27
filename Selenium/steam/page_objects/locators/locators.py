from selenium.webdriver.common.by import By
import pytest
import json

CONFIG_PATH = "Selenium\\steam\\tests\\test_data.json"

@pytest.fixture
def test_data():
    file = open(CONFIG_PATH)
    data = json.load(file)
    yield data

class SetLanguageLocators():

    current_lang = (By.XPATH, '//html[@class=" responsive"]')
    lang_menu_closed = (By.ID,'//span[@class="pulldown global_action_link"]')
    lang_menu_opened = (By.XPATH,'//span[@class="pulldown global_action_link focus"]')

    # def get_lang_locator(self, current_lang, test_data):
    #     lang_detect.translate("", current_lang, test_data["DEFAULT_LANG"])
    #     lang_locator = (By.XPATH, f'//a[@class="popup_menu_item tight" and text()="{target_lang}"]')
