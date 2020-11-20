import pytest
import time

from .pages.abonement_page import AbonementPage
from .pages.main_page import MainPage
from .pages.header_page import HeaderPage

class TestNab_Bug():
    def test_nab_bug(self, browser):
        main_page = MainPage(browser)
        abonement_page = AbonementPage(browser)
        header_page = HeaderPage(browser)

        main_page.open_main_page_link()
        header_page.goto_gamburger_login()

        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        main_page.open_main_page_link()

        abonement_page.open_abonement_page_link()

        # сделан для примера





