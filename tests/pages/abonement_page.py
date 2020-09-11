from .locators import AbonementPL
from .base_page import BasePage


class AbonementPage(BasePage):
    def goto_abonement_event(self):
        self.browser.find_by_css(AbonementPL.BTN_ABONEMENT_BUY).click()

    def check_abonement_event(self):
        assert self.browser.is_element_visible_by_css(
            AbonementPL.BTN_ABONEMENT_BUY), 'На странице мероприятий нет мероприятий'
