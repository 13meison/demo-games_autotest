import pytest
import time
import random
from .pages.main_page import MainPage


def test_stadium(browser):
    url = 'https://demo-games.infomatika.ru/'
    browser.visit(url)
    page = MainPage(browser)
    page.goto_event()
    assert browser.is_element_visible_by_css('#svg > g[price]', wait_time=5)
