import pytest


@pytest.fixture(scope='session')
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'


@pytest.fixture(scope='session')
def splinter_window_size():
    """Browser window size. (width, height)."""
    return (1920, 1080)

@pytest.fixture(scope='session')
def splinter_headless():
    return (False)

@pytest.fixture(scope='session')
def hide_welcome_popup(browser):
    browser.cookies.add({'accessHide': 'true'})

@pytest.fixture(scope='session')
def splinter_wait_time():
    return 10
