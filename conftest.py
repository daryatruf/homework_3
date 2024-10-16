import pytest
from selene import browser


@pytest.fixture
def browser_size():
    browser.config.window_height = 720
    browser.config.window_width = 1280


@pytest.fixture
def browser_open():
    browser.open('https://ya.ru/')

    yield

    browser.quit()
