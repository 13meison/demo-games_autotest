# -*- coding:utf-8 -*-

"""e2e tests."""
import pytest
import time
import random


@pytest.fixture(scope='session')
def splinter_window_size():
    """Browser window size. (width, height)."""
    return (1920, 1080)


# @pytest.fixture(scope='session')                                                         ---     фикстура которая добавляет параметры в куки
# def hide_welcome_popup(browser):
#     browser.cookies.add({'accessHide': 'true'})

def test_demo(browser):
    """Test using real browser."""
    url = "https://demo-games.infomatika.ru/"
    browser.visit(url)
    time.sleep(5)
    # browser.find_by_id("filter-date").click                                               ---     вызвать выпадющий виджет календаря
    # browser.find_by_id("filter-date").fill("01-10-2020 - 03-10-2020 ")                    ---     Ввести диапазон дат в фильтр
    # browser.find_by_css(".applyBtn").click()                                              ---     Применить диапазон дат фильтра (иногда лагает, потому что фильтр сворачивается)
    count_elements = browser.find_by_css('.events__buy')
    # assert len(count_elements) == 3, "не равняется 3"                                     ---     Проверка на правильность работы фильтра

    count_elements.click()
    count_sector = len(browser.find_by_css('#svg > g[price]'))

    num_of_random_sector = random.randrange(10, count_sector, 1)

    random_sector_selector = '#svg > g[price]:nth-child({})'.format(
        num_of_random_sector)
    # ({})'.format(num_of_random_sector)                                                     ---    используется как конкатенация строк

    browser.is_element_visible_by_css('#js-change-svg', wait_time=3)

    atr_random_sector_selector = browser.find_by_css(random_sector_selector)._element.get_attribute(
        'view_id')

    print(atr_random_sector_selector)
    browser.execute_script("$('g[view_id={}]').click()".format(
        atr_random_sector_selector))

    '''!!!!Что это снизу??????????????
    browser.execute_script("document.querySelector('#js-change-svg').scrollIntoView(true);")  
    browser.find_by_css(random_sector_selector).click()
    '''

    time.sleep(3)

    assert browser.is_element_visible_by_css(
        '#svg > g.active', wait_time=30), "не переключились на окно выбора мест"

    empty_places = browser.find_by_css('#svg > g.active')
    random_empty_place = empty_places[random.randrange(
        0, len(empty_places) - 1, 1)]
    atr_random_place_selector = browser.find_by_css(random_empty_place)._element.get_attribute(
        'id')

    print(atr_random_place_selector)
    browser.execute_script("$('g[id={}]').click()".format(
        atr_random_place_selector))

    # random_empty_place.click()
    assert browser.is_element_visible_by_css('.tickets_content', wait_time=30)


# ---------------------------------------------------------------------Вместо nth-child попробовать извлечь массив мест и секторов, с рендомным индексом

    # massiv_place_selector = browser.find_by_css('#svg > g[class="active"]')
    # massin_one_place_selector = massiv_place_selector[0]
    # print(massin_one_place_selector)

    # random_place_selector = '#svg > g[class="active"]:nth-child({})'.format(
    #     num_of_random_place)


# ---------------------------------------------------------------------Вместо nth-child попробовать извлечь массив мест и секторов, с рендомным индексом

    # atr_random_place_selector = browser.find_by_css(random_place_selector)._element.get_attribute('id')

    # print(atr_random_place_selector)

    # browser.execute_script("$('g[id={}]').click()".format(
    #     atr_random_place_selector))

    buy_button = browser.links.find_by_partial_href('/ru/orders/cart')
    buy_button.click()

    time.sleep(5)
