import pytest
import time


from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.locators import MainPL


class TestOne():
    def test_e2e_no_login(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)

        browser.visit(MainPL.MAIN_PAGE_URL)
        main_page.goto_event()

        sector_page.check_svg_sector()
        sector_page.select_empty_sector()
        sector_page.check_svg_places()

        sector_page.select_empty_place()
        sector_page.check_tickets_content_bar()
        header_page.check_number_basket()

        sector_page.goto_basket()
