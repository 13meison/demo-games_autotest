from .locators import HeaderPL
from .base_page import BasePage


class HeaderPage(BasePage):
    def check_number_basket(self):
        return self.browser.is_element_visible_by_css(HeaderPL.NUMBER_ITEMS_BASKET), "Значок количества товаров у корзины, не появился"

    def goto_gamburger_login(self):
        self.browser.find_by_css(HeaderPL.BTN_GAMBURGER).click()

    def goto_login(self):
        self.browser.find_by_css(HeaderPL.BTN_LOGIN).click()

    def input_form_login(self):
        self.browser.find_by_css(HeaderPL.FORM_LOGIN_EMAIL).fill(
            'mamaev@infomatika.ru')
        self.browser.find_by_css(HeaderPL.FORM_LOGIN_PASSWORD).fill(
            'mamaev@infomatika.ru')

    def btn_enter_login(self):
        self.browser.find_by_css(HeaderPL.BTN_FORM_LOGIN).click()

    def goto_menu_abonement(self):
        self.browser.links.find_by_partial_href(
            HeaderPL.MENU_ABONEMENT).click()
