import pytest
import time


from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.abonement_page import AbonementPage
from .pages.locators import MainPL


def test_check_abonement_event(browser):
    header_page = HeaderPage(browser)
    abonement_page = AbonementPage(browser)
    browser.visit(MainPL.MAIN_PAGE_URL)
    header_page.goto_menu_abonement()
    abonement_page.check_abonement_event()
