import pytest
from selene import browser

@pytest.fixture(scope='session')
def browser():
    browser.open('https://google.com')

    yield

@pytest.fixture(scope='session')
def browser_size(browser):
    driver.set_window_size(1200, 800)