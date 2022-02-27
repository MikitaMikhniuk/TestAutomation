from page_objects.pages.age_check_page import AgeVerificationPage
from framework.utils.navigation import navigate_to

from page_objects.pages.main_page import MainPage
from page_objects.pages.category_page import CategoryPage

import time

def test_max_discount(setup):
    driver = setup
    navigate_to(driver, "https://store.steampowered.com/")
    
    main_page = MainPage(driver)    
    main_page.verify_current_page_by_url("https://store.steampowered.com/")
    genre_main_page = main_page.navigate_menu("Категории", "Экшен")

    category_page = CategoryPage(driver)
    assert genre_main_page == category_page.verify_category_page()
    game_id_from_category_page = category_page.click_on_max_discount_game()

    

    # navigate_to(driver, "https://store.steampowered.com/agecheck/app/1091500/")

    # age_check = AgeVerificationPage(driver)
    # age_check.wait_for_age_verification_page()

    time.sleep(5)