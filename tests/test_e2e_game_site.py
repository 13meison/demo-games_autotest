import pytest
import time


from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.basket_page import BasketPage

class TestTwo1():
    def test_basket_clear_all(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)
        main_page.open_main_page_link()
        main_page.goto_event()
        sector_page.select_empty_sector()
        sector_page.select_empty_place()
        header_page.check_number_basket()
        sector_page.goto_basket()
        basket_page.delete_all_order()
        basket_page.check_basket_clear()

class TestThree():
    def test_basket_clear_all(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)
        main_page.open_main_page_link()
        main_page.goto_event()
        sector_page.select_empty_sector()
        sector_page.select_empty_place()
        header_page.check_number_basket()
        sector_page.goto_basket()
        basket_page.delete_all_tickets_event()
        basket_page.check_basket_clear()




# class TestOne():
#     def test_e2e_no_login(self, browser):
#         main_page = MainPage(browser)
#         sector_page = SectorPage(browser)
#         header_page = HeaderPage(browser)
#
#         browser.visit(MainPL.MAIN_PAGE_URL)
#         main_page.goto_event()
#
#         sector_page.check_svg_sector()
#         sector_page.select_empty_sector()
#         sector_page.check_svg_places()
#
#         sector_page.select_empty_place()
#         sector_page.check_tickets_content_bar()
#         header_page.check_number_basket()
#
#         sector_page.goto_basket()
