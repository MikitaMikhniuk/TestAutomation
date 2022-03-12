
class Locator():
    
    def topBarItem(self, section):
        locator_topBarItem = f'//a[contains(@class,"b-main-navigation__link")]/span[text()="{section}"]'  # Все работает! Каталог, Новости, Автобарахолка...
        return locator_topBarItem

    def pageSection(self, section):
        locator_pageSection = f'//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(), normalize-space("{section}"))]'  # Все работает! Каталог, Кошелек, Люди, Лайфстайл...
        return locator_pageSection

    def catalogHeader(self):
        locator_catalogHeader = f'//div[@class="catalog-navigation__title"]'
        return locator_catalogHeader

    def navClassifier(self, section):
        locator_navClassifier = f'//span[contains(@class,"catalog-navigation-classifier__item-title-wrapper") and translate(text(),' ',' ')="{section}"]'  # Все работает! Электроника, Компьютеры и сети
        return locator_navClassifier

    def navSubClass(self, section):
        locator_subClass = f'//div[contains(@class,"catalog-navigation-list__aside-title") and translate(normalize-space(text()),' ',' ')="{section}"]'  # Все работает! Моб. телефоны и аксессуары, Телевидение и видео
        return locator_subClass
    
    def asideItem(self, section):
        locator_asideItem = f'//span[contains(@class,"catalog-navigation-list__dropdown-title") and translate(normalize-space(text()),' ',' ')="{section}"]'  # Все работает! Телевизоры, Проекторы
        return locator_asideItem

    def itemCategoryHeader(self):
        locator_itemCategoryHeader = f'//h1[contains(@class,"schema-header__title")]'
        return locator_itemCategoryHeader

    def checkBoxLocator(self, keyword):
        locator_vendorCheckBox = f'//span[contains(@class,"schema-filter__checkbox-text") and text()="{keyword}"]'  # Любой чекбокс найдет!
        return locator_vendorCheckBox
    
    def minPrice(self):
        locator_minPrice = f'//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="от"]'  # Работает!
        return locator_minPrice

    def maxPrice(self):
        locator_maxPrice = f'//input[contains(@class,"schema-filter-control__item schema-filter__number-input schema-filter__number-input_price") and @placeholder="до"]'  # Работает!
        return locator_maxPrice

    def minSize(self, value):
        locator_minSize = f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]//option[@value="{value}"]' # To test
        return locator_minSize

    def maxSize(self, value):
        locator_maxSize = f'//div[contains(@class,"schema-filter-control schema-filter-control_select")]/following-sibling::div/select/option[@value="{value}"]' # To test
        return locator_maxSize

    def itemHeader(self):
        locator_itemHeader = f'//div[contains(@class,"schema-product__title")]//span'
        return locator_itemHeader

    def itemDescription(self):
        locator_itemDecription = f'//div[@class="schema-product__description"]/span'
        return locator_itemDecription

    def itemStartPrice(self):
        locator_itemStartPrice = f'//div[@class="schema-product__price"]/a'
        return locator_itemStartPrice

#_______________________________________________JUST IN CASE______________________________________________
# LOCATOR_pageSection = '//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(),"SECTION_NAME")]'
# locator_pageSection = '//header[@class="b-main-page-blocks-header-2 cfix"]//a[text()="SECTION_NAME"]'

# a = Locator()
# b = a.navClassifier("Компьютеры и сети")
# print(b)


# //span[translate(text(),' ',' ')='Бытовая техника']