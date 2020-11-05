from .locators import SectorPL
from .base_page import BasePage
import random


class SectorPage(BasePage):
    def check_svg_sector(self):
        assert self.browser.is_element_visible_by_css(
            SectorPL.SVG_SECTOR, wait_time=10), "СВГ схема выбора сектора, не отображена"

    def select_empty_sector(self):
        empty_sector = self.browser.find_by_css(SectorPL.SVG_EMPTY_SECTOR)
        random_empty_sector = empty_sector[random.randrange(
            0, len(empty_sector) - 1, 1)]
        random_empty_sector.click()

    def check_svg_places(self):
        assert self.browser.is_element_visible_by_css(
            SectorPL.SVG_PLACES, wait_time=10), "СВГ схема выбора мест, не отображена"

    def select_empty_place(self):
        empty_places = self.browser.find_by_css(
            SectorPL.SVG_EMPTY_PLACE, wait_time=10)
        random_empty_place = empty_places[random.randrange(
            0, len(empty_places) - 1, 1)]
        random_empty_place.click()

    def check_tickets_content_bar(self):
        assert self.browser.is_element_visible_by_css(
            SectorPL.TICKETS_CONTENT_BAR), "Блок с выбранными билетами не появился"

    def goto_basket(self):
        self.browser.links.find_by_partial_href(SectorPL.BTN_BASKET).click()

    def goto_btn_next_modal_windows(self):
        self.browser.find_by_css(SectorPL.BTN_NEXT_MODAL_WINDOWS).click()

    def scroll_nab_abonement_pop_up_down_200(self):
        self.browser.execute_script("document.querySelector('#js-popup-modal').scrollTo(0, 200)")
    def scroll_split_down_200(self):
        self.browser.execute_script("document.querySelector('.container').scrollTo(0, 200)")

    def zoom_minus(self):
        self.browser.find_by_css(SectorPL.BTN_ZOOM_MINUS).click()
        self.browser.find_by_css(SectorPL.BTN_ZOOM_MINUS).click()
        self.browser.find_by_css(SectorPL.BTN_ZOOM_MINUS).click()

    def zoom_plus(self):
        self.browser.find_by_css(SectorPL.BTN_ZOOM_PLUS).click()
        self.browser.find_by_css(SectorPL.BTN_ZOOM_PLUS).click()
        self.browser.find_by_css(SectorPL.BTN_ZOOM_PLUS).click()

    def goto_split_buy(self):
        self.browser.find_by_css(SectorPL.BTN_SPLIT_BUY).click()
