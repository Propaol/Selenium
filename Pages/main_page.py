from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Core.locators.locators_main_page import BaseLocatorsMainMenu as BaseLocators
from Core import cookies_class, local_storage
from selenium.webdriver import Keys
import time


class MainPage:
    def __init__(self, setup_driver):
        self.driver = setup_driver
        self.wait = WebDriverWait(setup_driver, 10)
        self.locator = BaseLocators()
        self.cookies = cookies_class.Cookies(setup_driver)
        self.local_storage = local_storage.LocalStorage(setup_driver)

    def go_to_category_page(self, locator):
        category = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        category.click()
        time.sleep(1)

    def get_current_url(self):
        return self.driver.current_url

    def get_header_text(self, locator):
        header = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return header.text

    def wait_until_element_appears(self, locator: tuple):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def send_text_to_element(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)


