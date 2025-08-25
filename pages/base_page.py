import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find element")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Get element text")
    def text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Click element")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Fill input field")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Wait for element to be visible")
    def wait_visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Wait for text to appear in element")
    def wait_text_of_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Wait for element to be clickable")
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step("Close modal window")
    def wait_order_modal_window_closed(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(locator)
        )

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", self.driver.find_element(*locator)
        )

    @allure.step("Check if element is visible")
    def visibility_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Get current window handle")
    def current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Wait")
    def wait(self):
        return WebDriverWait(self.driver, 10)

    @allure.step("Get all window handles")
    def window_handles(self):
        return self.driver.window_handles

    @allure.step("Switch to new window")
    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    @allure.step("Get current URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Drag and drop element")
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()
