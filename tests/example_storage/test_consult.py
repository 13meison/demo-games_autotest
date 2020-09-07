from selenium.webdriver.common.keys import Keys
import pytest
import time
import random


@pytest.fixture
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'



def test_demo(browser):
    url = 'http://base.consultant.ru/cons'
    browser.visit(url)
    browser.find_by_id('dictFilter').fill('нк ч2')
    browser.find_by_css('.smart_arrow').click()
    browser.windows.current = browser.windows[1]

    text_title = browser.title.lower()

    assert 'налоговый кодекс' in text_title, 'название страницы не содержит "налоговый кодекс"'
    assert 'часть вторая' in text_title, 'название страницы не содержит "часть вторая"'

    with browser.get_iframe(2) as iframe:
        title_elements = iframe.find_by_css('.document.content.flat').find_by_text('НАЛОГОВЫЙ КОДЕКС РОССИЙСКОЙ ФЕДЕРАЦИИ')
        assert len(title_elements) == 1, 'документ содержит "НАЛОГОВЫЙ КОДЕКС"'

        part_elements = iframe.find_by_css('.document.content.flat').find_by_text('ЧАСТЬ ВТОРАЯ')
        assert len(part_elements) == 1, 'документ содержит "ЧАСТЬ ВТОРАЯ"'

    toc_button = browser.find_by_css('.pageButtons').find_by_text('Оглавление')
    toc_button.click()

    assert browser.is_element_present_by_css('.page.contents'), 'не открылось оглавление'

    contents = browser.find_by_css('.page.contents')

    find_input = contents.find_by_name('dictFilter')

    find_input.fill('статья 163')
    find_input.type(Keys.ENTER)

    contents.find_by_css('.contentNameSel')

    time.sleep(10)
