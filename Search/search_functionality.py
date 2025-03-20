
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import random


class SearchFunctionality:
    def __init__(self, setup_driver):
        self.setup_driver = setup_driver
        self.wait = WebDriverWait(setup_driver, 10)

    def open_random_card(self, locator):
        '''Open Random Product'''
        card_element = self.setup_driver.find_elements(By.CLASS_NAME, locator)
        random_element = random.choice(card_element)
        random_element.click()

    def input_in_search_field(self, locator, text):
        '''Input on the search field'''
        search = self.wait.until(EC.presence_of_element_located((By.ID, locator)))
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

    def click_random_check_box(self, locator):
        '''Clicking to check box on the search menu'''
        check_box_element = self.setup_driver.find_elements(By.CLASS_NAME, locator)
        random_chech_box_element = random.choice(check_box_element)
        random_chech_box_element.click()

    def click_memory_check_box(self, locator):
        '''Clicking to a Memory check-box on the search menu'''
        memory_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_memory_chech_box_element = random.choice(memory_check_box_element)
        random_memory_chech_box_element.click()

    def click_brand_check_box(self, locator):
        '''Clicking to a Brand check-box on the search menu'''
        brand_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_brand_chech_box_element = random.choice(brand_check_box_element)
        random_brand_chech_box_element.click()

    def click_model_check_box(self, locator):
        '''Clicking to a Model check-box on the search menu'''
        model_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_model_chech_box_element = random.choice(model_check_box_element)
        random_model_chech_box_element.click()

    def click_price_check_box(self, locator):
        '''Clicking to a Price check-box on the search menu'''
        price_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_price_chech_box_element = random.choice(price_check_box_element)
        random_price_chech_box_element.click()

    def click_melhores_check_box(self, locator):
        '''Clicking to a Melhores check-box on the search menu'''
        melhores_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_melhores_chech_box_element = random.choice(melhores_check_box_element)
        random_melhores_chech_box_element.click()

    def click_estimate_check_box(self, locator):
        '''Clicking to an Estimate check-box on the search menu'''
        estimate_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_estimate_chech_box_element = random.choice(estimate_check_box_element)
        random_estimate_chech_box_element.click()


    def click_estado_check_box(self, locator):
        '''Clicking to an Estado check-box on the search menu'''
        estado_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_estado_chech_box_element = random.choice(estado_check_box_element)
        random_estado_chech_box_element.click()

    def click_ram_check_box(self, locator):
        '''Clicking to a RAM check-box on the search menu'''
        ram_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_ram_chech_box_element = random.choice(ram_check_box_element)
        random_ram_chech_box_element.click()

    def click_colour_check_box(self, locator):
        '''Clicking to a Colour check-box on the search menu'''
        colour_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_colour_chech_box_element = random.choice(colour_check_box_element)
        random_colour_chech_box_element.click()

    def click_mais_caract_check_box(self, locator):
        '''Clicking to a Mais Caracteristicas check-box on the search menu'''
        mais_caract_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_mais_caract_chech_box_element = random.choice(mais_caract_check_box_element)
        random_mais_caract_chech_box_element.click()


    def click_vendedores_check_box(self, locator):
        '''Clicking to a Vendedores check-box on the search menu'''
        vendedores_check_box_element = self.setup_driver.find_elements(By.XPATH, locator)
        random_vendedores_chech_box_element = random.choice(vendedores_check_box_element)
        random_vendedores_chech_box_element.click()