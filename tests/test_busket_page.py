import time

from Core.Locators.locators_busket import BusketPageLocators
from Core.Locators.locators_product_cards import ProductCards
from Pages.busket_page import Busket


def test_add_random_product_to_busket_from_main_page(setup_driver):
    '''Add random product to a busket'''
    main_page = Busket(setup_driver)
    main_page.add_random_product_to_busket_from_main_page_use_enter(ProductCards().add_random_product_from_main_page_to_busket3)
    assert BusketPageLocators().product_added_to_busket_popup

def test_open_busket_with_added_random_product(setup_driver):
    '''Check adding a random product on a busket page'''
    main_page = Busket(setup_driver)
    main_page.add_random_product_to_busket_from_main_page_use_enter(ProductCards().add_random_product_from_main_page_to_busket3)
    main_page.add_random_product_to_busket_from_main_page(BusketPageLocators().busket_icon_on_top_of_page)
    time.sleep(2)
    header_text = main_page.get_header_text('//h2')
    assert header_text == 'O meu carrinho'

