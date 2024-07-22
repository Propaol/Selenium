
from Core.Locators.locators_bebe_page import BebePageLocators
from Pages.bebe_page import Bebe


def test_fraldas_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().fraldas)

    fraldas_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/banho-e-higiene/fraldas?tipologia=Fraldas'
    assert bebe_page.get_current_url() == fraldas_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Fraldas'


def test_carrinhos_de_bebe_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().carrinhos)

    carrinhos_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/passeio/carrinhos-de-bebe'
    assert bebe_page.get_current_url() == carrinhos_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Carrinhos de Bebé'


def test_cadeiras_auto_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().cadeiras_auto)

    cadeiras_auto_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/passeio/cadeiras-auto-bebe'
    assert bebe_page.get_current_url() == cadeiras_auto_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Cadeiras Auto Bebé'


def test_intercomunicadores_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().intercomunicadores)

    intercomunicadores_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/protecao-e-saude-do-bebe/intercomunicadores-bebe'
    assert bebe_page.get_current_url() == intercomunicadores_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Intercomunicadores'


def test_bercos_e_colchoes_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().bercos)

    bercos_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/mobiliario-e-decoracao/bercos-e-colchoes'
    assert bebe_page.get_current_url() == bercos_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Berços e Colchões'


def test_espreguicadeira_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().espreguicadeira)

    espreguicadeira_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/mobiliario-e-decoracao/espreguicadeiras'
    assert bebe_page.get_current_url() == espreguicadeira_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Espreguiçadeiras'


def test_marsupios_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().marsupios)

    marsupios_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/passeio/marsupios-para-bebe'
    assert bebe_page.get_current_url() == marsupios_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Marsupios para Bebé'


def test_saude_do_bebe_page(bebe_page_fixture):
    bebe_page = Bebe(bebe_page_fixture)
    bebe_page.go_to_category_page(BebePageLocators().saude_do_bebe)

    saude_do_bebe_url = 'https://www.worten.pt/beleza-saude-e-bebe/bebe/protecao-e-saude-do-bebe'
    assert bebe_page.get_current_url() == saude_do_bebe_url

    header_text = bebe_page.get_header_text('//h1')
    assert header_text == 'Proteção e Saúde do Bebé'
