
import time
from Pages.personal_cabinet_page import PersonalCabinet
from Pages.main_page import MainPage
from Core import CONSTANTS
from Core.Locators.locators_personal_cabinet import PersonalCabiletLocators


def test_open_personal_cabinet_page(driver_login):
    '''Open Login Page'''
    driver = PersonalCabinet(driver_login)


def test_entre_login_fields(setup_driver):
    '''Test of Login to na Acc'''
    personal_cabinet = PersonalCabinet(setup_driver)
    personal_cabinet.open_login_page(PersonalCabiletLocators().click_to_login_icon)
    personal_cabinet.open_login_page(PersonalCabiletLocators().iniciar_login_session_button)
    personal_cabinet.input_in_login_field(PersonalCabiletLocators().email_field_id, PersonalCabiletLocators().pass_field, CONSTANTS.em, CONSTANTS.ps)
    time.sleep(1)
    dashboard_page = MainPage(setup_driver).get_current_url()
    assert dashboard_page == 'https://www.worten.pt/cliente/conta#/myDashboard'


