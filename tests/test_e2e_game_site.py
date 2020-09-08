import pytest
import time

from .pages.main_page import MainPage
from .pages.sector_page import SectorPage
from .pages.header_page import HeaderPage


def test_stadium(browser):
    url = 'https://demo-games.infomatika.ru/'
    browser.visit(url)

    page = MainPage(browser)
    page.goto_event()

    page_sector = SectorPage(browser)
    assert page_sector.check_svg_sector(), "СВГ схема выбора сектора, не отображена"
    page_sector.select_empty_sector()

    assert page_sector.check_svg_places(), "СВГ схема выбора мест, не отображена"

    page_sector.select_empty_place()
    assert page_sector.check_tickets_content_bar(
    ), "Блок с выбранными билетами не появился"

    page_header = HeaderPage(browser)
    assert page_header.check_number_basket(
    ), "Значок количества товаров у корзины, не появился"

    page_sector.goto_basket()
