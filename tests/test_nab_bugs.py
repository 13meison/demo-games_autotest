import pytest
import time

from .pages.abonement_page import AbonementPage
from .pages.main_page import MainPage
from .pages.header_page import HeaderPage
from .pages.abonement_page import AbonementPage
from .pages.basket_page import BasketPage
from .pages.sector_page import SectorPage
from .pages.main_page import MainPage

class TestNab_Bugs():
    def test_nab_bug_check_count_selected_match(self, browser):
        main_page = MainPage(browser)
        abonement_page = AbonementPage(browser)
        header_page = HeaderPage(browser)
        sector_page = SectorPage(browser)

        main_page.open_main_page_link()
        header_page.goto_gamburger_login()

        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        main_page.open_main_page_link()

        abonement_page.open_abonement_page_link()
        abonement_page.goto_abonement_event()
        abonement_page.plus_subscription_count()
        abonement_page.change_count_subscription_continue()
        abonement_page.check_count_subscription()
        abonement_page.check_btn_subscription_choose_seat()
        abonement_page.goto_btn_subscription_choose_seat()
        time.sleep(2)
        sector_page.select_empty_sector()
        sector_page.zoom_minus()
        time.sleep(2)
        sector_page.check_svg_places()
        sector_page.select_empty_place()
        time.sleep(2)
        sector_page.select_empty_place()
        sector_page.goto_btn_next_modal_windows()
        abonement_page.checkbox_select_all()
        time.sleep(2)

        abonement_page.check_subscription_selected_match_no_more_checked()
        time.sleep(2)
        abonement_page.checkbox_select_all()

    def test_4_match_10_procent_discount(self, browser):
        main_page = MainPage(browser)
        abonement_page = AbonementPage(browser)
        header_page = HeaderPage(browser)
        sector_page = SectorPage(browser)
        basket_page = BasketPage(browser)

        main_page.open_main_page_link()
        header_page.goto_gamburger_login()

        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        main_page.open_main_page_link()

        abonement_page.open_abonement_page_link()
        abonement_page.goto_abonement_event()
        abonement_page.plus_subscription_count()
        abonement_page.change_count_subscription_continue()
        abonement_page.check_count_subscription()
        abonement_page.check_btn_subscription_choose_seat()
        abonement_page.goto_btn_subscription_choose_seat()
        time.sleep(2)
        sector_page.select_empty_sector()
        sector_page.zoom_minus()
        time.sleep(2)
        sector_page.check_svg_places()
        sector_page.select_empty_place()
        time.sleep(2)
        sector_page.select_empty_place()
        sector_page.goto_btn_next_modal_windows()
        time.sleep(2)
        abonement_page.check_for_4_matches_10_percent_discount()

        abonement_page.goto_btn_subscription_buy()
        basket_page.delete_all_order()
        basket_page.check_basket_clear()




