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
    url = 'https://tickets.bckhimki.com/event/?id=191'
    browser.visit(url)
    # browser.is_element_visible_by_css(
    #     '#svg > switch > g[price]', wait_time=5)
    browser.is_element_visible_by_css(
        '#svg > switch > g > g[price]', wait_time=5)

    number_array = 0

    empty_sector = browser.find_by_css('#svg > switch > g > g[price]')
    name_empty_sector = empty_sector[number_array]['sector_name']
    print(name_empty_sector)
    empty_sector[number_array].click()

    assert browser.is_element_visible_by_css(
        '#svg > g.active', wait_time=30), "не переключились на окно выбора мест"

    name_sector = browser.find_by_css('tspan').text
    index_name_sector = name_sector.find(name_empty_sector)
    print(index_name_sector)
    print(name_sector)
    assert index_name_sector != -1, 'Названия секторов не совпадают'

    # assert name_empty_sector == name_sector, 'Названия секторов не совпадают'
    time.sleep(5)
