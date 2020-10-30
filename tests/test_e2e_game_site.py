import pytest
import time


from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.basket_page import BasketPage
from .pages.abonement_page import AbonementPage


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
        basket_page.check_page_load()
        # time.sleep(2)
        basket_page.delete_all_tickets_event()
        basket_page.check_basket_clear()

    def test_no_login_buy_event_delete_order(self, browser):
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
        basket_page.check_page_load()
        # time.sleep(2)
        basket_page.delete_all_order()
        basket_page.check_basket_clear()

    def test_login_buy_event_delete_order(self, browser):
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
        basket_page.check_page_load()
        # time.sleep(2)
        basket_page.delete_all_order()
        basket_page.check_basket_clear()

class TestNabAbonementBuy():
    def test_nab_abonement_buy(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)
        abonement_page = AbonementPage(browser)

        main_page.open_main_page_link()
        header_page.goto_gamburger_login()
        time.sleep(2)

        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        time.sleep(2)
        # cookies = browser.cookies.all()
        # coockie_login = 'session2'
        # assert coockie_login in cookies, 'no login'
        header_page.check_user_login()

        abonement_page.open_abonement_page_link()
        time.sleep(2)
        abonement_page.check_abonement_event()
        abonement_page.goto_abonement_event()
        abonement_page.change_count_subscription()
        abonement_page.change_count_subscription_next()
        abonement_page.plus_subscription_count()
        abonement_page.change_count_subscription_continue()
        abonement_page.check_btn_subscription_choose_seat()
        abonement_page.goto_btn_subscription_choose_seat()
        sector_page.select_empty_sector()
        sector_page.select_empty_place()
        sector_page.select_empty_place()
#Здесь остановился, тест не доделан
# команда вызова теста
# poetry run pytest --tb=line -v test_e2e_game_site.py::TestNabAbonementBuy


