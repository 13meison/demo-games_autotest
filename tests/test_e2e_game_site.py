import pytest
import time
import random
from pages.locators.py import MainPageLocators


@pytest.fixture(scope='session')
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'


@pytest.fixture(scope='session')
def splinter_window_size():
    """Browser window size. (width, height)."""
    return (1920, 1080)


@pytest.fixture(scope='session')
def hide_welcome_popup(browser):
    browser.cookies.add({'accessHide': 'true'})


def test_stadium(browser):
    url = 'https://demo-games.infomatika.ru/'
    browser.visit(url)
    browser.MainPageLocators.BTN_events_buy.click()

    assert browser.is_element_visible_by_css('#svg > g[price]', wait_time=5)
