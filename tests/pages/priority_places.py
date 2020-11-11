from .locators import PriorityPL
from .base_page import BasePage
import random

class PriorityPage(BasePage):
    def check_btn_goto_priority_places(self):
        assert self.browser.links.find_by_partial_href(PriorityPL.BTN_SELECT_PRIORITY_PLACES), 'Кнопка перехода к приоритетным местам недоступна'
    def goto_priority_places(self):
        self.browser.links.find_by_partial_href(PriorityPL.BTN_SELECT_PRIORITY_PLACES).click()
    def checkbox_select_all(self):
        self.browser.find_by_css(PriorityPL.CHECKBOX_ALL).click()

    def checkbox_select_place(self):
        self.browser.find_by_css(PriorityPL.CHECKBOX_PLACES_ONE).click()
        self.browser.find_by_css(PriorityPL.CHECKBOX_PLACES_TWO).click()

    def click_btn_buy_priority(self):
        self.browser.find_by_css(PriorityPL.BTN_BUY_PRIORITY).click()


        # checkbox_odd = self.browser.find_by_css(PriorityPL.CHECKBOX_PLACES_ODD)
        # print(checkbox_odd[0])
        # #тут вопросец, не понятно как выделить 1 элемент из объекта
        # checkbox_odd = self.browser.find_by_css(PriorityPL.CHECKBOX_PLACES_ODD).click()


