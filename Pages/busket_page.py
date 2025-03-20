from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from Core.Locators.locators_busket import BusketPageLocators
from selenium.webdriver import Keys
import random
import time


class Busket:
    def __init__(self, setup_driver):
        self.setup_driver = setup_driver
        self.wait = WebDriverWait(setup_driver, 10)

    def add_random_product_to_busket_from_main_page(self, locator):
        add_random_product = self.setup_driver.find_elements(By.XPATH, locator)
        random_product = random.choice(add_random_product)
        random_product.click()


    def add_random_product_to_busket_from_main_page_use_enter(self, locator):
        add_random_product = self.setup_driver.find_elements(By.XPATH, locator)
        random_product = random.choice(add_random_product)
        random_product.send_keys(Keys.ENTER)

    def get_header_text(self, locator):
        header = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return header.text

