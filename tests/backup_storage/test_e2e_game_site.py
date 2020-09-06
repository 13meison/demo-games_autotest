import pytest
import time
import random


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
    browser.find_by_css('.events__buy').click()

    browser.is_element_visible_by_css('#svg > g[price]', wait_time=0.1)

    empty_sector = browser.find_by_css('#svg > g[price]')
    random_empty_sector = empty_sector[random.randrange(
        0, len(empty_sector) - 1, 1)]
    random_empty_sector.click()

    assert browser.is_element_visible_by_css(
        '#svg > g.active', wait_time=30), "не переключились на окно выбора мест"

    empty_places = browser.find_by_css('#svg > g.active')
    random_empty_place = empty_places[random.randrange(
        0, len(empty_places) - 1, 1)]
    random_empty_place.click()
    assert browser.is_element_visible_by_css(
        '.tickets__content', wait_time=30), 'блок с выбраными местами не появился'
    assert browser.is_element_visible_by_css(
        '.header__link-count'), 'У корзины не появился значок кол-ва товаров'
    buy_button = browser.links.find_by_partial_href('/ru/orders/cart')
    buy_button.click()

    time.sleep(5)
