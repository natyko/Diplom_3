import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from api.user_api import UserAPI, delete_test_user, create_test_user, login
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urllib.parse import urljoin

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://stellarburgers.nomoreparties.site")
LOGIN_URL = f"{BASE_URL}/login"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use for tests"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
        drv = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        if headless:
            options.add_argument("--headless")
        drv = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(10)
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def registered_user():
    api = UserAPI()
    user = api.generate_test_user()
    response = api.register_user(user)
    assert response.status_code == 200, f"Failed to register: {response.text}"
    yield user
    api.login_user(user)
    api.delete_user()

# @pytest.fixture
# def login_user(driver):
#     user = create_test_user()
#     login(driver, user)
#     WebDriverWait(driver, 10).until(expected_conditions.url_to_be(BASE_URL))
#     yield user
#     delete_test_user(user)
@pytest.fixture
def login_user(driver):
    user = create_test_user()
    login(driver, user)
    try:
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url.rstrip("/") == BASE_URL.rstrip("/")
        )
    except TimeoutException:
        driver.save_screenshot("login_redirect_failed.png")
        raise TimeoutException(f"Expected URL to be {BASE_URL}, but got {driver.current_url}")
    yield user
    delete_test_user(user)

@pytest.fixture(scope="function")
def logged_in_user(driver, registered_user):
    login_page = LoginPage(driver, LOGIN_URL)
    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])

    main_page = MainPage(driver, BASE_URL)
    assert main_page.is_element_present(
        main_page.locators.BURGER_CONSTRUCTOR, timeout=10
    )

    return registered_user


@pytest.fixture
def create_order(driver, logged_in_user):
    """Create an order and return the order number"""
    main_page = MainPage(driver, BASE_URL)
    main_page.open()
    assert main_page.is_element_present(main_page.locators.BURGER_CONSTRUCTOR, timeout=10), \
        "Burger constructor is not visible"
    main_page.add_ingredient_to_burger()
    main_page.click_place_order_button()
    order_number = main_page.get_order_number()
    assert order_number, "Order number must be retrieved"
    return order_number.replace("#", "").strip()