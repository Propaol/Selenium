from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class Bebe:
    def __init__(self, setup_driver):
        self.locator_header = ('//h1')
        self.setup_driver = setup_driver
        self.wait = WebDriverWait(setup_driver, 15)

    def go_to_category_page(self, locator):
        category = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        category.click()
        time.sleep(1)

    def get_current_url(self):
        return self.setup_driver.current_url

    def get_header_text(self, locator):
        header = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return header.text
