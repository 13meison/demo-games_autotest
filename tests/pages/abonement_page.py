from .locators import AbonementPL
from .base_page import BasePage
from .main_page import MainPL


class AbonementPage(BasePage):
    def open_abonement_page_link(self):
        self.browser.visit(AbonementPL.ABONEMENT_PAGE_URL)

    def goto_abonement_event(self):
        self.browser.find_by_css(MainPL.BTN_ABONEMENT_BUY).click()

    def check_abonement_event(self):
        assert self.browser.is_element_visible_by_css(
            MainPL.BTN_ABONEMENT_BUY), 'На странице мероприятий нет мероприятий'

    def check_btn_subscription_choose_seat(self):
        assert self.browser.is_element_visible_by_css(AbonementPL.BTN_SUBSCRIPTION_CHOOSE), 'Нет мероприятий в абонементе'
    def goto_btn_subscription_choose_seat(self):
        self.browser.find_by_css(AbonementPL.BTN_SUBSCRIPTION_CHOOSE).click()

    def change_count_subscription(self):
        self.browser.find_by_css(AbonementPL.SUBSCRIPTION_COUNT).click()
    def change_count_subscription_next(self):
        self.browser.links.find_by_partial_href(AbonementPL.SUBSCRIPTION_COUNT_BTN_NEXT).click()
    def plus_subscription_count(self):
        self.browser.find_by_css(AbonementPL.BTN_SUBSCRIPTION_PLUS).click()
    def minus_subscription_count(self):
        self.browser.find_by_css(AbonementPL.BTN_SUBSCRIPTION_MINUS).click()
    def change_count_subscription_continue(self):
        self.browser.find_by_css(AbonementPL.SUBSCRIPTION_COUNT_BTN_CONTINUE).click()

