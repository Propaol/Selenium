
from Pages.main_page import MainPage
from Core.Locators.locators_main_page import BaseLocatorsMainMenu


def test_open_worten(setup_driver):
    '''Open the Worten Main screen'''
    driver = setup_driver


def test_open_menu(products_menu):
    '''Open the Products menu'''
    menu = products_menu


def test_servico_menu(servico_menu):
    '''Open the Servico menu'''
    servico = servico_menu


def test_open_bebe_page(setup_driver, wait):
    '''Test to open the Bebe page.
    Work with Cookies.
    Work with LocalStorage'''

    main_page = MainPage(setup_driver)

    main_page.cookies.add_cookie({'name': 'sales_features_2', 'value': 'air_conditioning'})
    main_page.local_storage.set_item('some value in local storage', 'ValuE1')

    main_page.go_to_category_page(BaseLocatorsMainMenu().bebe)

    bebe_page = 'https://www.worten.pt/beleza-saude-e-bebe/bebe'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == bebe_page
    assert header_text == 'Bebé'

    example_value = main_page.local_storage.get_item('some value in local storage')
    assert example_value == 'ValuE1'

    main_page.cookies.delete_all_cookies()
    main_page.local_storage.remove_item('some value in local storage')


def test_open_electrodomesticos_page(setup_driver, wait):
    '''Test to open the Electrodomesticos page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().electrodomesticos)

    electrodomesticos_page = 'https://www.worten.pt/grandes-eletrodomesticos/encastre'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == electrodomesticos_page
    assert header_text == 'Encastre'


def test_open_desporto_outdoor_page(setup_driver, wait):
    '''Test to open the Desporto Outdoor page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().desporto_outdoor)

    desporto_outdoor_page = 'https://www.worten.pt/desporto-mobilidade-outdoor/desporto'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == desporto_outdoor_page
    assert header_text == 'Desporto'


def test_open_casa_decoracao_page(setup_driver, wait):
    '''Test to open the Casa Decoracao page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().casa_decoracao)

    casa_decoracao_page = 'https://www.worten.pt/casa'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == casa_decoracao_page
    assert header_text == 'Casa e Decoração'


def test_open_bricolage_page(setup_driver, wait):
    '''Test to open the Bricolage page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().bricolage)

    bricolage_page = 'https://www.worten.pt/bricolage'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == bricolage_page
    assert header_text == 'Bricolage'


def test_open_perfumaria_page(setup_driver, wait):
    '''Test to open the Parfumaria page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().perfumaria)

    perfumaria_page = 'https://www.worten.pt/perfumaria-cosmetica-e-beleza'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == perfumaria_page
    assert header_text == 'Perfumaria, Cosmética e Beleza'


def test_open_moda_page(setup_driver, wait):
    '''Test to open the Moda page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().moda)

    moda_page = 'https://www.worten.pt/moda'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == moda_page
    assert header_text == 'Moda'


def test_open_animals_page(setup_driver, wait):
    '''Test to open the Animals page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().animals)

    animals_page = 'https://www.worten.pt/animais-de-estimacao'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == animals_page
    assert header_text == 'Animais de Estimação'


def test_open_jogos_page(setup_driver, wait):
    '''Test to open the Jogos page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().jogos)

    jogos_page = 'https://www.worten.pt/jogos-e-brinquedos'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == jogos_page
    assert header_text == 'Jogos e Brinquedos'


def test_open_jardim_page(setup_driver, wait):
    '''Test to open the Jardim page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().jardim)

    jardim_page = 'https://www.worten.pt/jardim'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == jardim_page
    assert header_text == 'Jardim'


def test_open_escritorio_page(setup_driver, wait):
    '''Test to open the Escritorio page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().escritorio)

    escritorio_page = 'https://www.worten.pt/escritorio-e-papelaria'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == escritorio_page
    assert header_text == 'Escritório e Papelaria'


def test_open_tv_and_smartphones_page(setup_driver, wait):
    '''Test to open the TV and Smartphones page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().tv_and_smartphones)

    tv_and_smartphones_page = 'https://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == tv_and_smartphones_page
    assert header_text == 'Telemóveis e Smartphones'


def test_open_computers_and_laptops_page(setup_driver, wait):
    '''Test to open the Computers and Laptops page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().computers_and_laptops)

    computers_and_laptops_page = 'https://www.worten.pt/informatica-e-acessorios/computadores'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == computers_and_laptops_page
    assert header_text == 'Computadores'


def test_open_tv_page(setup_driver, wait):
    '''Test to open the TV page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().tv)

    tv_page = 'https://www.worten.pt/tv-video-e-som/tvs'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == tv_page
    assert header_text == 'TVs'


def test_open_gaming_page(setup_driver, wait):
    '''Test to open the Gaming page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().gaming)

    gaming_page = 'https://www.worten.pt/gaming'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == gaming_page
    assert header_text == 'Gaming'


def test_open_maquinas_lavar_page(setup_driver, wait):
    '''Test to open the Maquinas page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().maquinas_lavar)

    maquinas_lavar_page = 'https://www.worten.pt/grandes-eletrodomesticos/maquinas-de-roupa'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == maquinas_lavar_page
    assert header_text == 'Máquinas de Roupa'


def test_open_preparacio_de_alimentos_page(setup_driver, wait):
    '''Test to open the Preparacio de Alimentos page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().preparacio_de_alimentos)

    preparacio_de_alimentos_page = 'https://www.worten.pt/pequenos-eletrodomesticos/preparacao-de-alimentos'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == preparacio_de_alimentos_page
    assert header_text == 'Preparação de Alimentos'


def test_open_aspiradores_page(setup_driver, wait):
    '''Test to open the Aspiradores page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().aspiradores)

    aspiradores_page = 'https://www.worten.pt/pequenos-eletrodomesticos/aspiradores'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == aspiradores_page
    assert header_text == 'Aspiradores'


def test_open_aquecedores_conditioners_page(setup_driver, wait):
    '''Test to open the Conditioners page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().aquecedores_conditioners)

    aquecedores_conditioners_page = 'https://www.worten.pt/grandes-eletrodomesticos/climatizacao'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == aquecedores_conditioners_page
    assert header_text == 'Climatização'


def test_open_smartwatches_page(setup_driver, wait):
    '''Test to open the Smartwatches page'''
    main_page = MainPage(setup_driver)
    main_page.go_to_category_page(BaseLocatorsMainMenu().smartwatches)

    smartwatches_page = 'https://www.worten.pt/telemoveis-e-pacotes-tv/smartwatches'
    header_text = main_page.get_header_text('//h1')

    assert main_page.get_current_url() == smartwatches_page
    assert header_text == 'Smartwatches'
