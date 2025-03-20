
class BusketPageLocators:
    '''Locators on the Busket page'''
    def __init__(self):
        self.product_added_to_busket_popup = '//p[contains(text(), "Produto adicionado ao carrinho")]'
        self.busket_icon_on_top_of_page = '//li[@class="main-nav__cart"]'
