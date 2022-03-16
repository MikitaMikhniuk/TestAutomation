Feature: Catalog TV Filter
    In order to filter desired TV's from the Onliner catalog,
    As a regular user
    I want to navigate to TV's catalog page and filter them
    based on some params

    Scenario: Navigate to catalog
        Given website "https://www.onliner.by/"
        When main page is opened
        Then click top bar "Каталог" button
        Then verify that main page is "Каталог"
        
    Scenario: Navigate to TV's section
        When "Каталог" page is opened
        Then navigate to "Электроника" -> "Телевидение и видео" -> "Телевизоры"
        Then verify that page is "Телевизоры"
        
    Scenario: Apply filters and verify results
        When current page is "Телевизоры"
        Then click on 'Samsung' filter
        Then set max price "1500"
        Then set resolution to "1920x1080 (Full HD)"
        Then set size range between '400' and '500'
        Then assert filter results