from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.common.exceptions import TimeoutException

from config import PROFILE_URL
from locators.locators import BasePageLocators, MainPageLocators
import allure
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url=None, timeout=10):
        self.locators = None
        self.driver = driver
        self.url = url if url is not None else getattr(self, "url", None)
        print(f"DEBUG: {self.__class__.__name__} initialized with url={self.url!r}")
        assert isinstance(self.url, str), f"url is not a string: {self.url!r}"
        self.timeout = timeout

    def wait_until_clickable(self, locator, timeout=10):
        with allure.step(f"Ожидание кликабельно элемента: {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )

    def open(self):
        assert isinstance(self.url, str), f"url is not a string: {self.url!r}"
        print("DEBUG: Opening URL:", self.url, type(self.url))
        self.driver.get(self.url)

    def wait(self, condition, timeout=None):
        """Wait for a specific condition"""
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_element_visible(self, locator):
        with allure.step(f"Ожидание видимости элемента: {locator}"):
            return self.wait(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator, timeout=None):
        """Check if element is present on the page"""
        if timeout is None:
            timeout = self.timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator, timeout=None):
        """Check if element is visible on the page"""
        if timeout is None:
            timeout = self.timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator, timeout=10):
        with allure.step(f"Проверка, что элемент видим: {locator}"):
            try:
                WebDriverWait(self.driver, timeout).until(
                    expected_conditions.visibility_of_element_located(locator)
                )
                return self.driver.find_element(*locator).is_displayed()
            except TimeoutException:
                return False

    def is_element_clickable(self, locator, timeout=None):
        """Check if element is clickable"""
        if timeout is None:
            timeout = self.timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False

    def find_element(self, locator, timeout=None):
        """Find element with wait"""
        if timeout is None:
            timeout = self.timeout

        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element


    def find_elements(self, locator, timeout=None):
        """Find elements with wait"""
        if timeout is None:
            timeout = self.timeout

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click_element(self, locator, timeout=None):
        """Click element with wait"""
        element = self.find_element(locator, timeout)
        element.click()

    def click(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            WebDriverWait(self.driver, timeout=10).until(
                expected_conditions.element_to_be_clickable(locator)
            ).click()


    def send_keys_to_element(self, locator, keys, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.clear()
            element.send_keys(keys)
        except TimeoutException:
            print(f"Timeout while waiting for element: {locator}")
            raise

    def get_element_text(self, locator, timeout=None):
        """Get element text with wait"""
        element = self.find_element(locator, timeout)
        return element.text

    def wait_for_url_contains(self, url_fragment, timeout=None):
        """Wait for URL to contain specified fragment"""
        if timeout is None:
            timeout = self.timeout

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url_fragment))
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_be(self, url, timeout=None):
        """Wait for URL to be exactly as specified"""
        if timeout is None:
            timeout = self.timeout

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def is_closed(self, locator, timeout=5):
        with allure.step(f"Проверка, что элемент скрыт: {locator}"):
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(locator)
                )
                return True
            except TimeoutException:
                try:
                    element = self.driver.find_element(*locator)
                    return not element.is_displayed()
                except:
                    return True

    def go_to_feed(self):
        """Go to feed page"""
        self.click_element(BasePageLocators.FEED_BUTTON)

    # In base_page.py - Move import inside method
    def go_to_profile(self):
        """Navigate to profile page"""
        with allure.step("Navigate to profile page"):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)
            )
            self.click_element(MainPageLocators.PROFILE_BUTTON)
            from pages.profile_page import ProfilePage
            return ProfilePage(self.driver, PROFILE_URL)

    def go_to_main_page_via_logo(self):
        """Go to main page by clicking on the logo"""
        self.click_element(BasePageLocators.LOGO)

    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        with allure.step(
            f"Drag and drop element {source_locator} on element {target_locator}"
        ):
            wait = WebDriverWait(self.driver, timeout)

            source = wait.until(EC.presence_of_element_located(source_locator))
            target = wait.until(EC.presence_of_element_located(target_locator))

            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(target).release().perform()

    def get_text(self, locator):
        with allure.step(f"Get element text: {locator}"):
            element = self.wait(EC.visibility_of_element_located(locator))
            return element.text

    def is_opened(self):
        with allure.step(f"Проверить, что страница открыта по URL: {self.url}"):
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.url_to_be(self.url)
            )

    def wait_for_element_visible_by_locator(self, locator, timeout=10):
        """Wait until the given element is visible on the page"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
