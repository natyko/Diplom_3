from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    RESET_LINK = (
        By.XPATH,
        "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']",
    )
    LOGIN_FORM = (By.NAME, "name")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")


class PasswordRecoveryPageLocators:
    # EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    EMAIL_INPUT_RECOVERY = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    RESET_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")


class MainPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    INGREDIENT_PRICE = (
        By.XPATH,
        "//div[contains(@class, 'BurgerIngredient_ingredient__')]",
    )
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Ingredient modal
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    INGREDIENT_MODAL_CLOSE = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]",
    )
    BUN_TOP = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    BUN_BOTTOM = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_bottom')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_CONFIRMATION_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_CONFIRMATION_CLOSE = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]",
    )
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    BASKET_LIST = (By.XPATH, "//ul[contains(@class, 'basket__list')]")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredient')]")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter__num')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_DETAILS = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'basket__list')]")


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderCard_orderCard')]")
    ORDER_NUMBER_TEXT = (
        By.XPATH,
        "//p[contains(@class, 'text text_type_digits-default')]",
    )
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(),'История заказов')]")
    ORDER_HISTORY_BLOCK = (By.CLASS_NAME, "OrderHistory_list")


class FeedPageLocators:
    # Order feed
    USER_ORDER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")
    # USER_ORDER = "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]"
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")
    ORDER_NUMBER_TEXT = (By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS_COLUMN = (By.XPATH, "//div[contains(text(), 'В работе')]/following-sibling::div")
    DONE_COLUMN = (By.XPATH, "//div[contains(text(), 'Готовы')]/following-sibling::div")
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_STARTED_TEXT = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")
    ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")
    ORDER_DETAILS = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    ORDER_LABEL = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    # DONE_TOTAL = (By.XPATH,  '//p[text()="Выполнено за все время:"]/following-sibling::p')
    DONE_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    # DONE_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")


class OrderDetailsPageLocators:
    # Order modal
    # ORDER_MODAL = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]")
    ORDER_STATUS = (By.XPATH, "//p[contains(@class, 'text text_type_main-default')]")
    ORDER_INGREDIENTS = (
        By.XPATH,
        "//div[contains(@class, 'OrderDetails_ingredients')]",
    )
    ORDER_TOTAL_PRICE = (By.XPATH, "//div[contains(@class, 'OrderDetails_price')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
