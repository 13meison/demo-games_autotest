from .locators import MainPL
from .base_page import BasePage


class MainPage(BasePage):
    def open_main_page_link(self):
        self.browser.visit(MainPL.MAIN_PAGE_URL)
    def goto_event(self):
        self.browser.find_by_css(MainPL.BTN_EVENTS_BUY).click()

    def check_user_profile_dropdown(self):
        assert self.browser.is_element_visible_by_css(
            MainPL.USER_PROFILE_DROPDOWN)
