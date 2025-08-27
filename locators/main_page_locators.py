from selenium.webdriver.common.by import By


class MainPageLocators:
    # "Personal Account" button on main page
    PROFILE_BUTTON = (By.XPATH, "//a[@href = '/account']")

    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_LINK = (
        By.XPATH,
        '//p[contains(@class, "AppHeader_header__linkText") and text()="Лента Заказов"]',
    )

    # Order feed
    FIRST_ORDER_IN_FEED = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]/li[1]")
    ORDER_INFO = (
        By.XPATH,
        '//div[contains(@class, "Modal_orderBox") and contains(@class, "Modal_modal__contentBox")]',
    )
    ORDER_FEED_HEADER = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    MY_ORDER_IN_ORDER_FEED = (
        By.XPATH,
        "//p[contains(@class, 'text') and contains(@class, 'text_type_main-default') and text()='Выполнен']",
    )
    ORDERS_FOR_ALL_TIME = (
        By.XPATH,
        '//p[contains(normalize-space(),"Выполнено за все время")]/following-sibling::p[1]',
    )
    ORDERS_FOR_TODAY = (
        By.XPATH,
        '//p[contains(normalize-space(),"Выполнено за сегодня")]/following-sibling::p[1]',
    )
    ORDER_IN_PROCESS_IN_FEED = (
        By.XPATH,
        '//div/ul[2]/li[contains(@class,"text_type_digits-default")]',
    )
    ORDER_IN_MODAL_WINDOW = (
        By.XPATH,
        '//h2[contains(@class, "Modal_modal__title_shadow") and contains(@class, "Modal_modal__title") and contains(@class, "text_type_digits-large")]',
    )
    MODAL_OPENED = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened') and .//div[contains(@class,'Modal_orderBox')]]",
    )
    CRATER_BUN = (
        By.XPATH,
        "//img[contains(@alt,'Краторная') and contains(@alt,'N-200i')]",
    )
    CLOSE_MODAL_WINDOW_BUTTON = (By.XPATH, '//button/*[name()="svg"]')
    BURGER_INGREDIENTS = (
        By.XPATH,
        '//ul[contains(@class, "BurgerConstructor_basket__list")]',
    )
    BUN_COUNTER = (By.XPATH, '//p[text()="2"]')
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    EXTRA_ORDER_MODAL_WINDOW = (By.XPATH, '//*[contains(@class, "Modal_modal__loading")]')

    SAUCES_LINK = (By.XPATH, "//span[text() = 'Соусы']")
    BUNS_LINK = (By.XPATH, "//span[text() = 'Булки']")
    FILLINGS_LINK = (By.XPATH, "//span[text() = 'Начинки']")

    # Additional order feed locators for dynamic searching
    ORDER_FEED_TEXT_BOX_DIGITS = (
        By.XPATH,
        '//div[contains(@class, "OrderFeed_textBox")]/ul/li[contains(@class, "digits")]',
    )
    TEXT_TYPE_DIGITS_DEFAULT = (By.XPATH, '//li[contains(@class, "text_type_digits-default")]')
    ALL_ORDERS_READY = (By.XPATH, '//*[text()="Все текущие заказы готовы!"]')
