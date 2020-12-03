import time



from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage
from .pages.basket_page import BasketPage
from .pages.abonement_page import AbonementPage
from .pages.priority_places import PriorityPage


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
        header_page.check_user_login()

        abonement_page.open_abonement_page_link()
        time.sleep(2)
        abonement_page.check_abonement_event()
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
        abonement_page.check_not_visible_old_price()
        abonement_page.check_price_nab_zero()
        abonement_page.checkbox_select_all()

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

        abonement_page.goto_btn_subscription_buy()
        basket_page.delete_all_order()
        basket_page.check_basket_clear()
        '''Предустановка для успешного прохождения этого теста:
        на странице самого мероприятия, должен быть включен чекбокс "Включить все" в аккаунте тестируемого пользователя 
        '''

class TestSplitAbonementBuy():
    def test_split_abonement_buy(self, browser):
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
        header_page.check_user_login()

        abonement_page.open_abonement_page_link()
        time.sleep(2)
        abonement_page.check_abonement_event()
        abonement_page.goto_split_abonement_event()
        time.sleep(2)
        sector_page.split_first_plan_select_empty_sector()
        sector_page.scroll_to_center_svg_element()
        sector_page.check_svg_sector()
        time.sleep(2)
        sector_page.select_split_empty_place()
        time.sleep(2)
        sector_page.goto_split_next()
        sector_page.split_second_plan_select_empty_sector()
        time.sleep(5)
        sector_page.select_split_empty_place()
        # sector_page.goto_btn_next_modal_windows()

        # time.sleep(2)
        # sector_page.scroll_to_center_svg_element()


        # sector_page.split_second_plan_select_empty_sector()
        # sector_page.select_split_empty_place()
        sector_page.goto_split_buy()
        basket_page.delete_all_order()
        basket_page.check_basket_clear()

class TestPriorityPlaces():
    def test_priority_places(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)
        abonement_page = AbonementPage(browser)
        priority_page = PriorityPage(browser)


        main_page.open_main_page_link()
        header_page.goto_gamburger_login()
        time.sleep(2)
        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        time.sleep(2)
        header_page.check_user_login()
        header_page.goto_gamburger_login()
        header_page.goto_priority_places()

        priority_page.check_btn_goto_priority_places()
        priority_page.goto_priority_places()
        priority_page.checkbox_select_all()
        priority_page.checkbox_select_place()
        priority_page.click_btn_buy_priority()
        time.sleep(2)
        header_page.check_number_basket()
        basket_page.delete_all_order()
        basket_page.check_basket_clear()


        time.sleep(2)


class TestIntegration():
    def test_event_and_nab_buy(self, browser):
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
        header_page.check_user_login()

        abonement_page.open_abonement_page_link()
        time.sleep(2)
        abonement_page.check_abonement_event()
        abonement_page.goto_abonement_event()
        abonement_page.plus_subscription_count()
        abonement_page.change_count_subscription_continue()

        abonement_page.check_count_subscription()
        # abonement_page.checkbox_select_all()
        abonement_page.check_btn_subscription_choose_seat()
        abonement_page.goto_btn_subscription_choose_seat()
        time.sleep(2)
        sector_page.select_empty_sector()
        time.sleep(2)
        sector_page.check_svg_places()
        sector_page.zoom_minus()
        sector_page.select_empty_place()
        time.sleep(2)
        sector_page.select_empty_place()
        sector_page.goto_btn_next_modal_windows()
        abonement_page.goto_btn_subscription_buy()

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

        basket_page.delete_all_order()
        basket_page.check_basket_clear()

    def test_event_and_priority_buy(self, browser):
        main_page = MainPage(browser)
        sector_page = SectorPage(browser)
        header_page = HeaderPage(browser)
        basket_page = BasketPage(browser)
        priority_page = PriorityPage(browser)

        main_page.open_main_page_link()
        header_page.goto_gamburger_login()
        time.sleep(2)
        header_page.goto_login()
        header_page.input_form_login()
        header_page.btn_enter_login()
        time.sleep(2)
        header_page.check_user_login()

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

        header_page.goto_gamburger_login()
        header_page.goto_priority_places()

        priority_page.check_btn_goto_priority_places()
        priority_page.goto_priority_places()
        priority_page.checkbox_select_all()
        priority_page.checkbox_select_place()
        priority_page.click_btn_buy_priority()

        basket_page.delete_all_order()
        basket_page.check_basket_clear()


# команда вызова теста
# poetry run pytest --tb=line -v test_e2e_game_site.py

