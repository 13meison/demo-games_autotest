import pytest
import time


from .pages.main_page import MainPage
from .pages.header_page import HeaderPage
from .pages.locators import MainPL
from .pages.locators import AbonementPL


def test_login(browser):
    main_page = MainPage(browser)
    header_page = HeaderPage(browser)

    browser.visit(MainPL.MAIN_PAGE_URL)
    header_page.goto_login()
    header_page.input_form_login()
    header_page.btn_enter_login()
    time.sleep(10)
    main_page.check_user_profile_dropdown()
