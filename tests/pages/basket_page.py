from .locators import BasketPL
from .base_page import BasePage


class BasketPage(BasePage):
    def delete_all_order(self):
        self.browser.find_by_css(BasketPL.BTN_ALL_CLEAR).click()
    def delete_all_tickets_event(self):
        self.browser.find_by_css(BasketPL.BTN_TICKETS_EVENT_DELETE).click()
    def check_basket_clear(self):
        assert self.browser.is_element_visible_by_css(BasketPL.TEXT_CLEAR_BASKET), 'Корзина не пуста'
    def check_page_load(self):
        self.browser.find_by_css(BasketPL.ELEMENT_PAGE_LOAD)


