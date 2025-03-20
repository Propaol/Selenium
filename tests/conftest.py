from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import random

def get_random_value():
    return str(random.randint(100000,300000))

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.worten.pt/')
    driver.maximize_window()
    #driver.add_cookie()
    wait = WebDriverWait(driver, 10)
    accept_cookie = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="button--primary button--md button--black button--icon-left button"]')))
    accept_cookie.click()
    time.sleep(1)
    yield driver
    driver.quit()


@pytest.fixture
def driver_smartphones():
    driver = webdriver.Chrome()
    driver.get('https://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    accept_cookie = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="button--primary button--md button--black button--icon-left button"]')))
    accept_cookie.click()
    time.sleep(2)
    yield driver
    driver.quit()


@pytest.fixture()
def products_menu(setup_driver):
    driver = setup_driver
    chose_products = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             '//button[@aria-label="Produtos"]'))
    )
    chose_products.click()
    yield driver


@pytest.fixture()
def servico_menu(setup_driver):
    driver = setup_driver
    servico_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             '//button[@aria-label="Serviços"]'))
    )
    servico_menu.click()
    yield driver

@pytest.fixture()
def wait(setup_driver):
    wait  = WebDriverWait(setup_driver, 5)
    yield wait

@pytest.fixture()
def bebe_page_fixture():
    driver = webdriver.Chrome()
    driver.get('https://www.worten.pt/beleza-saude-e-bebe/bebe')
    wait = WebDriverWait(driver, 10)
    accept_cookie = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//button[@class="button--primary button--md button--black button--icon-left button"]')))
    accept_cookie.click()
    time.sleep(1)
    yield driver
    driver.quit()

@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    driver.get('https://www.worten.pt/cliente/conta#/myLogin')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    accept_cookie = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="button--primary button--md button--black button"]')))
    accept_cookie.click()
    time.sleep(2)
    yield driver
    driver.quit()

@pytest.fixture
def setup_driver_cookie(driver):
    driver.get('https://www.worten.pt/')
    print(driver.get_cookie('_ga_6QK0BMVT8Q'))
    generated_cookie = get_random_value()
    driver.add_cookie({'name':'pespatron', 'value':f'__ua{generated_cookie}'})
    print(driver.get_cookie('pespatron'))
    driver.execute_script("window.localStorage['feature_send_flow_confirmation_v2'] = 'False';")
    print(driver.execute_script("return window.localStorage['feature_send_flow_confirmation_v2'];"))
    yield setup_driver_cookie(driver)

