from .locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):
    def goto_event(self):
        self.browser.find_by_css(MainPageLocators.BTN_events_buy).click()
