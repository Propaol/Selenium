import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalCabinet:
    def __init__(self, driver_login):
        self.setup_driver = driver_login
        self.wait = WebDriverWait(driver_login, 10)

    def get_header_text(self, locator):
        header = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return header.text

    def open_login_page(self, locator):
        open_login_page = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        time.sleep(1)
        open_login_page.click()

    def input_in_login_field(self, locator1, locator2, text1, text2):
        input_text = self.wait.until(EC.presence_of_element_located((By.ID, locator1)))
        input_text.send_keys(text1)
        input_text.send_keys(Keys.TAB)
        input_text = self.wait.until(EC.presence_of_element_located((By.ID, locator2)))
        input_text.send_keys(text2)
        input_text.send_keys(Keys.ENTER)
