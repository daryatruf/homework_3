from selene import be, have, browser


def test_search(browser_size, browser_open):
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="OrganicTitleContentSpan organic__title"]').should(
        have.text('User-oriented Web UI browser tests in Python'))


def test_no_search_result(browser_size, browser_open):
    browser.element('[name="text"]').should(be.blank).type(';lkdcfojwedgvfhjbdfs').press_enter()
    browser.element('[class="EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))
