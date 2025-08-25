import pytest
from selenium import webdriver
from config import PAGE_URLS
from locators.login_page_locators import LoginPageLocators
from api.user_api import UserAPI
from api.order_api import OrderAPI


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(PAGE_URLS["login"])

    yield driver
    driver.execute_script("window.localStorage.clear();")
    driver.quit()


@pytest.fixture
def driver_signed_in():
    driver = webdriver.Chrome()
    driver.get(PAGE_URLS["login"])
    driver.find_element(*LoginPageLocators.INPUT_EMAIL_AUTH).send_keys(
        "123@yopmail.com"
    )
    driver.find_element(*LoginPageLocators.INPUT_PASSWORD_AUTH).send_keys("privet123$")
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()

    yield driver
    driver.execute_script("window.localStorage.clear();")
    driver.quit()


@pytest.fixture
def test_user_api():
    # Create a test user via API for testing
    user_api = UserAPI()
    test_user_data = user_api.generate_test_user()

    # Register user via API
    register_response = user_api.register_user(test_user_data)
    if register_response.status_code == 200:
        # Login to get tokens
        login_response = user_api.login_user(
            test_user_data["email"], test_user_data["password"]
        )
        if login_response.status_code == 200:
            test_user_data["access_token"] = user_api.access_token
            test_user_data["api_client"] = user_api

    yield test_user_data

    # Cleanup delete user
    try:
        if hasattr(user_api, "access_token") and user_api.access_token:
            user_api.delete_user()
    except:
        pass


@pytest.fixture
def order_api_with_auth(test_user_api):
    # Order API client with authenticated user
    if "access_token" in test_user_api:
        return OrderAPI(test_user_api["access_token"])
    else:
        return OrderAPI()  # Return unauthenticated client if user setup failed
