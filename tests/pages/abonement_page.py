from .locators import AbonementPL
from .base_page import BasePage
from .main_page import MainPL


class AbonementPage(BasePage):
    def open_abonement_page_link(self):
        self.browser.visit(AbonementPL.ABONEMENT_PAGE_URL)

    def goto_abonement_event(self):
        self.browser.find_by_css(MainPL.BTN_ABONEMENT_BUY).click()
    def goto_split_abonement_event(self):
        self.browser.find_by_css(MainPL.BTN_SPLIT_BUY).click()

    def check_abonement_event(self):
        assert self.browser.is_element_visible_by_css(
            MainPL.BTN_ABONEMENT_BUY), 'На странице мероприятий нет мероприятий'

    def check_btn_subscription_choose_seat(self):
        assert self.browser.is_element_visible_by_css(AbonementPL.BTN_SUBSCRIPTION_CHOOSE), 'Нет мероприятий в абонементе'

    '''     Скролл элемента на верх страницы
    def test_test(self):
        self.browser.execute_script('document.querySelector("'+ AbonementPL.BTN_SUBSCRIPTION_CHOOSE +'").scrollIntoView(true)')
            Скролл элемента на центр старницы
    def scroll_to_btn_subscription_choose_element(self):
        self.browser.execute_script('document.querySelector("'+ AbonementPL.BTN_SUBSCRIPTION_CHOOSE +'").scrollIntoView({block: "center", inline: "nearest"})')

    '''
    def goto_btn_subscription_choose_seat(self):
        self.browser.execute_script(
            'document.querySelector("' + AbonementPL.BTN_SUBSCRIPTION_CHOOSE + '").scrollIntoView({block: "center", inline: "nearest"})')
        self.browser.find_by_css(AbonementPL.BTN_SUBSCRIPTION_CHOOSE).click()

    def goto_btn_subscription_buy(self):
        self.browser.find_by_css(AbonementPL.BTN_SUBSCRIPTION_BUY).click()



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

    def check_count_subscription(self):
        subscription_count = self.browser.find_by_css(AbonementPL.TEXT_COUNT_SUBSCRIPTION).text
        assert int(subscription_count) == 2, 'Неверное количество абонементов'


