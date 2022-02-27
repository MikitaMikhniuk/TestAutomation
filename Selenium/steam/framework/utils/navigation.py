from selenium.webdriver.common.by import By
from framework.utils.nav_config import Nav

def navigate_to(driver, URL):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//html')
    Nav.LANG = element.get_attribute("lang")
    print(Nav.LANG)        