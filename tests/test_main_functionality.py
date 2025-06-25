import allure

from locators.locators import MainPageLocators
from pages.main_page import MainPage
from config import LOGIN_URL, BASE_URL, FEED_URL


@allure.feature("Main Functionality")
class TestMainFunctionality:

    @allure.title("Test navigation to constructor")
    @allure.description("Test that user can navigate to constructor from other pages")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.click_constructor_button()
        assert main_page.is_constructor_visible()

    @allure.title("Test navigation to feed")
    @allure.description("Test that user can navigate to feed page")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.click_order_feed_button()
        assert driver.current_url == FEED_URL, "Failed to navigate to feed page"

    @allure.title("Test ingredient modal")
    @allure.description("Test that clicking on an ingredient shows details modal")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.click_on_ingredient(0)  # Click on the first ingredient
        assert (
            main_page.is_ingredient_modal_open()
        ), "Ingredient modal should be displayed after clicking an ingredient"
        assert main_page.is_ingredient_details_visible()

    @allure.title("Test closing ingredient modal")
    @allure.description(
        "Test that ingredient modal can be closed by clicking the X button"
    )
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.click_on_ingredient(0)
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_details_closed()

    @allure.title("Test ingredient counter")
    @allure.description("Test that adding ingredient increases its counter")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.add_ingredient_to_burger()
        assert main_page.is_ingredient_counter_incremented()


@allure.description(
    "Создание заказа авторизованным пользователем и проверка отображения окна деталей"
)
def test_create_order_when_logged_in(self, driver, logged_in_user):
    main_page = MainPage(driver, BASE_URL)
    main_page.open()

    # Ensure login
    main_page.login_if_needed()

    # Add ingredient and place order
    main_page.open()
    main_page.add_ingredient_to_burger()
    main_page.click_place_order_button()

    # Wait for confirmation
    assert main_page.is_order_details_visible(), "Order details modal not visible"

