from .locators import HeaderPL
from .base_page import BasePage


class HeaderPage(BasePage):
    def check_number_basket(self):
        return self.browser.is_element_visible_by_css(HeaderPL.NUMBER_ITEMS_BASKET)
