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

    def check_not_visible_old_price(self):
        assert self.browser.is_element_not_visible_by_css(AbonementPL.TEXT_OLD_PRICE), 'Старая цена не исчезла'
    def check_price_nab_zero(self):
        price = self.browser.find_by_css(AbonementPL.TEXT_PRICE).text
        assert price == '0', 'the price was not reset'

    def check_subscription_selected_match_no_more_checked(self):
        checked = self.browser.find_by_css(AbonementPL.TEXT_SUBSCRIPTION_CHECKED).text
        selected = self.browser.find_by_css(AbonementPL.TEXT_SUBSCRIPTION_SELECTED).text
        assert int(checked) >= int(selected), 'there are more selected matches than active ones'
    def check_for_4_matches_10_percent_discount(self):
        discount_price = self.browser.find_by_css(AbonementPL.TEXT_PRICE).text
        old_price = self.browser.find_by_css(AbonementPL.TEXT_OLD_PRICE).text
        assert int(old_price) * 0.1 == int(old_price) - int(discount_price), 'скидка не равна 10%'
    '''     Скролл элемента на верх страницы
    def test_test(self):
        self.browser.execute_script('document.querySelector("'+ AbonementPL.BTN_SUBSCRIPTION_CHOOSE +'").scrollIntoView(true)')
            Скролл элемента на центр старницы
    def scroll_to_btn_subscription_choose_element(self):
        self.browser.execute_script('document.querySelector("'+ AbonementPL.BTN_SUBSCRIPTION_CHOOSE +'").scrollIntoView({block: "center", inline: "nearest"})')

    '''
    def checkbox_select_all(self):
        self.browser.find_by_css(AbonementPL.CHECK_BOX_ALL).click()

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


