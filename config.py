"""Constants used across the project."""

# Base URLs
BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = "https://stellarburgers.nomoreparties.site/api"
MAIN_URL = "https://stellarburgers.nomoreparties.site"
# PROFILE_URL = "https://stellarburgers.nomoreparties.site/profile"
PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"
LOGIN_URL = f"{BASE_URL}/login"
FEED_URL =f"{BASE_URL}/feed"

# Page URLs
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
ACCOUNT_URL = f"{BASE_URL}/account/profile"

# API URLs
REGISTER_API_URL = f"{API_URL}/auth/register"
LOGIN_API_URL = f"{API_URL}/auth/login"
LOGOUT_API_URL = f"{API_URL}/auth/logout"  # Renamed for consistency
TOKEN_API_URL = f"{API_URL}/auth/token"  # Added token refresh endpoint
USER_API_URL = f"{API_URL}/auth/user"  # Renamed for consistency
ORDERS_API_URL = f"{API_URL}/orders"  # Renamed for consistency
ORDERS_ALL_API_URL = f"{API_URL}/orders/all"  # Renamed for consistency
INGREDIENTS_API_URL = f"{API_URL}/ingredients"  # Renamed for consistency
PASSWORD_RESET_API_URL = f"{API_URL}/password-reset"  # Renamed for consistency
PASSWORD_RESET_CONFIRM_API_URL = (
    f"{API_URL}/password-reset/reset"  # Renamed for consistency
)

# Path constants (for page initialization)
MAIN_PAGE_PATH = "/"
LOGIN_PAGE_PATH = "/login"
REGISTER_PAGE_PATH = "/register"
FORGOT_PASSWORD_PATH = "/forgot-password"
RESET_PASSWORD_PATH = "/reset-password"
PROFILE_PATH = "/account/profile"
PROFILE_ORDERS_PATH = "/account/order-history"
FEED_PATH = "/feed"

# Test user credentials
TEST_USER = {
    "email": "naty@yopmail.com",
    "password": "password123",
    "name": "Test User",
    "invalid_password": "123",
}

# For generating random test users
TEST_EMAIL_DOMAIN = "yopmail.com"

# Test data
TEST_INGREDIENT_NAME = "Краторная булка N-200i"
TEST_SAUCE_NAME = "Соус Spicy-X"

# Ingredient IDs from API documentation example
TEST_INGREDIENT_IDS = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]

# Expected messages (for assertions)
SUCCESS_MESSAGE = "success"
USER_ALREADY_EXISTS_MESSAGE = "User already exists"
FIELDS_REQUIRED_MESSAGE = "Email, password and name are required fields"
INCORRECT_CREDENTIALS_MESSAGE = "email or password are incorrect"
SUCCESSFUL_LOGOUT_MESSAGE = "Successful logout"
PASSWORD_RESET_EMAIL_SENT_MESSAGE = "Reset email sent"
PASSWORD_RESET_SUCCESS_MESSAGE = "Password successfully reset"
AUTHORIZATION_REQUIRED_MESSAGE = "You should be authorised"

# Timeout
DEFAULT_TIMEOUT = 10

# Browser types
CHROME = "chrome"
FIREFOX = "firefox"

# Browser options
HEADLESS = "--headless"
WINDOW_SIZE = "--window-size=1920,1080"

# Order status
ORDER_STATUS_DONE = "done"
