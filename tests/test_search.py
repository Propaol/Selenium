
from Core.Locators.locators_product_cards import ProductCards
from Search.search_function import SearchFunctionality
from Core.Locators.locators_search import Search


def test_open_random_product(driver_smartphones):
    '''Test for open random product on the "Smartphones" category'''
    random_product = SearchFunctionality(driver_smartphones)
    random_product.open_random_card(ProductCards().random_product_locator)


def test_input_some_in_search_field(setup_driver):
    '''Test of using the "SEARCH" field'''
    search_field = SearchFunctionality(setup_driver)
    search_field.input_in_search_field(Search().search_field, 'OnePlus 11')


def test_click_to_a_check_box(driver_smartphones):
    '''Test for open random product on the "Smartphones" category'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_random_check_box(Search().search_menu_check_box_container)


def test_click_to_a_memory_check_box(driver_smartphones):
    '''Test Clicking to a Memory check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_memory_check_box(Search().search_menu_memory)


def test_click_to_a_brand_check_box(driver_smartphones):
    '''Test Clicking to a Brand check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_brand_check_box(Search().search_menu_brand)


def test_click_to_a_model_check_box(driver_smartphones):
    '''Test Clicking to a Model check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_model_check_box(Search().search_menu_model)


def test_click_to_a_price_check_box(driver_smartphones):
    '''Test Clicking to a Price check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_price_check_box(Search().search_menu_price)


def test_click_to_a_melhores_check_box(driver_smartphones):
    '''Test Clicking to a Melhores check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_melhores_check_box(Search().search_menu_melhores)



def test_click_to_an_estimate_check_box(driver_smartphones):
    '''Test Clicking to an Estimate check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_estimate_check_box(Search().search_menu_estimate)


def test_click_to_an_estado_check_box(driver_smartphones):
    '''Test Clicking to an Estado check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_estado_check_box(Search().search_menu_estado)
    #time.sleep(10)

def test_click_to_an_ram_check_box(driver_smartphones):
    '''Test Clicking to an RAM check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_ram_check_box(Search().search_menu_ram)
    #time.sleep(10)

def test_click_to_a_colour_check_box(driver_smartphones):
    '''Test Clicking to a Colour check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_colour_check_box(Search().search_menu_colour)
    #time.sleep(10)

def test_click_to_a_mais_caract_check_box(driver_smartphones):
    '''Test Clicking to a Mais Caracteristacas check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_mais_caract_check_box(Search().search_menu_mais_caracteristicas)
    #time.sleep(10)

def test_click_to_a_vendedores_check_box(driver_smartphones):
    '''Test Clicking to a Vendedores check-box on the search menu'''
    smartphones_page = SearchFunctionality(driver_smartphones)
    smartphones_page.click_vendedores_check_box(Search().search_menu_vendedores)
    #time.sleep(10)