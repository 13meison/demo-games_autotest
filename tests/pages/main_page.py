from .locators import MainPL
from .base_page import BasePage


class MainPage(BasePage):
    def goto_event(self):
        self.browser.find_by_css(MainPL.BTN_EVENTS).click()
