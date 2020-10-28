import pytest
import time


from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.basket_page import BasketPage

# class TestTwo1():
#     def test_basket_clear_all(self, browser):
#         main_page = MainPage(browser)
#         sector_page = SectorPage(browser)
#         header_page = HeaderPage(browser)
#         basket_page = BasketPage(browser)
#         main_page.open_main_page_link()
#         main_page.goto_event()
#         sector_page.select_empty_sector()
#         sector_page.select_empty_place()
#         header_page.check_number_basket()
#         sector_page.goto_basket()
#         basket_page.delete_all_order()
#         basket_page.check_basket_clear()
#
# def test_basket_clear_all(browser):
#     main_page = MainPage(browser)
#     sector_page = SectorPage(browser)
#     header_page = HeaderPage(browser)
#     basket_page = BasketPage(browser)
#     main_page.open_main_page_link()
#     main_page.goto_event()
#     sector_page.select_empty_sector()
#     sector_page.select_empty_place()
#     header_page.check_number_basket()
#     sector_page.goto_basket()
#     basket_page.delete_all_order()
#     basket_page.check_basket_clear()
#
#
# class TestThree():
#     def test_basket_clear_all(self, browser):
#         main_page = MainPage(browser)
#         sector_page = SectorPage(browser)
#         header_page = HeaderPage(browser)
#         basket_page = BasketPage(browser)

#         main_page.open_main_page_link()
#         main_page.goto_event()

#         sector_page.select_empty_sector()
#         sector_page.select_empty_place()
#         header_page.check_number_basket()
#         sector_page.goto_basket()
#         basket_page.delete_all_tickets_event()
#         basket_page.check_basket_clear()
#
#
#
#
class TestEventBuy():
    def test_no_login_buy_event_delete_event(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)

        main_page.open_main_page_link()
        main_page.goto_event()
        sector_page.check_svg_sector()
        sector_page.select_empty_sector()
        sector_page.check_svg_places()

        sector_page.select_empty_place()
        sector_page.check_tickets_content_bar()

        header_page.check_number_basket()
        sector_page.goto_basket()
        basket_page.delete_all_tickets_event()
        basket_page.check_basket_clear()

def test_no_login_buy_event_delete_order(browser):
    main_page = MainPage(browser)
    sector_page = SectorPage(browser)
    header_page = HeaderPage(browser)
    basket_page = BasketPage(browser)

    main_page.open_main_page_link()
    main_page.goto_event()
    sector_page.check_svg_sector()
    sector_page.select_empty_sector()
    sector_page.check_svg_places()

    sector_page.select_empty_place()
    sector_page.check_tickets_content_bar()

    header_page.check_number_basket()
    sector_page.goto_basket()
    basket_page.delete_all_order()
    basket_page.check_basket_clear()

def test_login_buy_event_delete_order(browser):
    main_page = MainPage(browser)
    sector_page = SectorPage(browser)
    header_page = HeaderPage(browser)
    basket_page = BasketPage(browser)

    main_page.open_main_page_link()
    header_page.goto_gamburger_login()

    header_page.goto_login()
    header_page.input_form_login()
    header_page.btn_enter_login()

    main_page.open_main_page_link()
    main_page.goto_event()
    sector_page.check_svg_sector()
    sector_page.select_empty_sector()
    sector_page.check_svg_places()

    sector_page.select_empty_place()
    sector_page.check_tickets_content_bar()

    header_page.check_number_basket()
    sector_page.goto_basket()
    basket_page.delete_all_order()
    basket_page.check_basket_clear()