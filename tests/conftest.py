import os
import time

import allure
import pytest

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attachments


@allure.step('Конфигурация тестов')
@pytest.fixture(scope='function', autouse=False)
def test_browser_configuration():
    browser.config.base_url = os.getenv('selene.base_url', 'https://auto.drom.ru')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 2
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "114.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # driver = webdriver.Remote(
    #     command_executor="http://172.17.104.155:4444/wd/hub",
    #     options=options)

    # browser.config.driver = driver
    yield
    browser.config.hold_browser_open = False
    # attachments.add_html(browser)
    # attachments.add_screenshot(browser)
    # attachments.add_logs(browser)
    # attachments.add_video(browser)


@allure.step('Чистим данные после теста добавления авто в избранное')
@pytest.fixture(scope='function', autouse=False)
def clear_test_artifacts():
    yield
    elements = browser.all('[class="removeBookmark"]')
    for i in elements:
        i.click()


@pytest.fixture(scope='function', autouse=False)
def browser_config_selenium():
    driver = webdriver.Chrome(executable_path='D:\\ATProject\\Drom\\chromedriver.exe')
    yield
    driver.close()
