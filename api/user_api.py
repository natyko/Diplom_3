# File: api/user_api.py

import uuid
import requests

from config import LOGIN_URL
from locators.locators import PasswordRecoveryPageLocators
from pages.password_recovery_page import PasswordRecoveryPage

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


class UserAPI:
    """API client for user-related operations"""

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json"}
        self.auth_token = None

    def generate_test_user(self):
        email = f"test_{uuid.uuid4()}@yandex.ru"
        password = "123456"
        name = "Test User"
        return {"email": email, "password": password, "name": name}

    def register_user(self, user_data):
        response = requests.post(f"{self.base_url}/auth/register", json=user_data)
        return response

    def login_user(self, user_data):
        response = requests.post(f"{self.base_url}/auth/login", json=user_data)
        if response.status_code == 200:
            self.auth_token = response.json()["accessToken"].split()[-1]
            self.headers["Authorization"] = f"Bearer {self.auth_token}"
        return response

    def delete_user(self):
        if self.auth_token:
            return requests.delete(f"{self.base_url}/auth/user", headers=self.headers)
        return None

    @staticmethod
    def login_via_ui(driver, user_data):
        from locators.locators import LoginPageLocators

        driver.get("LOGIN_URL")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(
            user_data["email"]
        )
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            user_data["password"]
        )
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def create_test_user():
    def generate_email():
        return f"test_{uuid.uuid4()}@yandex.ru"

    user = {
        "email": generate_email(),
        "password": "123456",
        "name": "Test User"
    }
    requests.post(f"{BASE_URL}/auth/register", json=user)
    return user


def delete_test_user(user):
    token = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user["email"], "password": user["password"]
    }).json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(f"{BASE_URL}/auth/user", headers=headers)

def login(driver, user):
    driver.get(LOGIN_URL)
    driver.find_element(*PasswordRecoveryPageLocators.EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*PasswordRecoveryPageLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element("xpath", "//button[text()='Войти']").click()