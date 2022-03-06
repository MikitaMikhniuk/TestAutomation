from selenium.webdriver.common.by import By
from framework.utils.nav_config import Nav


def navigate_to(driver, URL):
    """
    Navigation method used to define current lang and send it to lang_utis.

    Input-> URL (str).

    """
    
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//html')
    Nav.LANG = element.get_attribute("lang")
