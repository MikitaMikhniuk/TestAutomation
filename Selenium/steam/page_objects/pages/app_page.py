
from framework.base.base_page import BasePage


class AppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_app_id(self):
        pass