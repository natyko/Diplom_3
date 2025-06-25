import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from config import LOGIN_URL, BASE_URL, PROFILE_URL


@allure.feature("User Profile")
class TestUserProfile:

    @allure.title("Navigate to order history")
    @allure.description(
        "User should be able to view their order history after logging in"
    )
    def test_navigate_to_order_history(self, driver, logged_in_user):
        main_page = MainPage(driver, BASE_URL)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver, PROFILE_URL)
        profile_page.go_to_order_history_section()

        WebDriverWait(driver, 10).until(EC.url_contains("order-history"))
        assert "order-history" in driver.current_url

    @allure.title("Logout from profile")
    @allure.description("User should be redirected to login page after logout")
    def test_logout(self, driver, logged_in_user):
        main_page = MainPage(driver, BASE_URL)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver, PROFILE_URL)
        profile_page.logout()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert (
            LOGIN_URL in driver.current_url
        ), "User should be redirected to login page after logout"

    @allure.title("Navigate to profile section")
    @allure.description(
        "Logged in user should be able to navigate to the profile section"
    )
    def test_go_to_profile(self, driver, logged_in_user):
        MainPage(driver).click_profile_button()
        assert ProfilePage(driver).is_opened()

    @allure.title("Order history URL check")
    @allure.description(
        "Verify URL contains 'order-history' after navigating to order history"
    )
    def test_go_to_order_history(self, driver, logged_in_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.go_to_order_history_section()
        WebDriverWait(driver, 10).until(EC.url_contains("order-history"))
        assert "order-history" in driver.current_url

    @allure.title("Logout second attempt")
    @allure.description("Ensure logout button works as expected")
    def test_logout_second_attempt(self, driver, logged_in_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.logout()

        login_page = LoginPage(driver, LOGIN_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert login_page.is_opened()


    @allure.title("Test navigation to profile page")
    @allure.description("Test that logged in user can navigate to profile page")
    def test_navigate_to_profile(self, driver, logged_in_user):
        # Create main page object
        main_page = MainPage(driver, BASE_URL)
        main_page.open()

        # Navigate to profile
        profile_page = main_page.go_to_profile()

        # Verify navigation worked
        assert profile_page.is_profile_form_visible(), "Profile form not visible"
        assert driver.current_url.startswith(PROFILE_URL), "Failed to navigate to profile page"

    # @allure.title("Test navigation to profile page")
    # @allure.description("Test that logged in user can navigate to profile page")
    # def test_navigate_to_profile(self, driver, logged_in_user):
    #     # Create main page object
    #     main_page = MainPage(driver, BASE_URL)
    #     main_page.open()
    #     profile_page = main_page.go_to_profile()
    #
    #     assert driver.current_url == PROFILE_URL, "Failed to navigate to profile page"
    #     assert profile_page.is_opened(), "Profile page should be loaded"
    #     assert profile_page.is_element_present(profile_page.locators.PROFILE_LINK), "Profile link should be visible"

