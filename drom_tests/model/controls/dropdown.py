from selene import have, be
from selene.support.shared import browser


def select(selector, element, option):
    element.should(be.clickable).click()
    element.type(option)
    browser.all(selector).by(
        have.text(option)
    ).first.click()
