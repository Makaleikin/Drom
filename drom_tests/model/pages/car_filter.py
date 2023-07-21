import os
from typing import Tuple
import allure
from selene.support.shared import browser
from selene import browser, have, be, command
from webdriver_manager.core import driver

from drom_tests.model.controls import dropdown


class CarFilter:
    @allure.step('Открываем страницу продажи автомобилей')
    def given_opened(self):
        browser.open('https://auto.drom.ru/')

    @allure.step('Выбираем марку Toyota')
    def select_brand(self, option):
        brand_element = browser.element('[placeholder="Марка"]')
        dropdown_selector = '[class="css-1r0zrug e1uu17r80"]'
        dropdown.select(dropdown_selector, brand_element, option)

    @allure.step('Выбираем модель Harrier')
    def select_model(self, option):
        model_element = browser.element('[placeholder="Модель"]')
        dropdown_selector = '[class="css-1r0zrug e1uu17r80"]'
        dropdown.select(dropdown_selector, model_element, option)

    @allure.step('Выбираем топливо - гибрид')
    def select_type_of_fuel(self, option):
        fuel_element = '[class="css-17vx1of e1x0dvi10"]'
        fuel = '[aria-label="Топливо"]'
        browser.element(fuel).should(be.visible).click()
        browser.all(fuel_element).by(have.exact_text(option)).first.click()

    @allure.step('Выставляем год от 2007')
    def select_year_from(self, year):
        browser.all('[class="css-me79aa e75dypj1"]').element_by(have.text('Год от')).click()
        browser.all('[class="css-17vx1of e1x0dvi10"]').element_by(have.text(year)).click()

    @allure.step('Проставляем чекбокс - "Непроданные"')
    def select_checkbox_unsold(self):
        browser.element('[for="sales__filter_unsold"]').click()

    @allure.step('Раскрываем "Расширенный поиск"')
    def show_advanced_search(self):
        browser.element('[class="ezmft1z0 css-1q5ta30 e104a11t0"]').click()

    @allure.step('Скроллим к "Пробег"')
    def scroll_to_mileage(self):
        browser.element('[placeholder="от, км"]').perform(command.js.scroll_into_view)

    @allure.step('Указываем пробег от 1 км')
    def set_mileage_from(self, mileage):
        browser.element('[placeholder="от, км"]').type(mileage)

    @allure.step('Жмем "Показать"')
    def show_results(self):
        browser.all('[class="css-tjza12 e1lm3vns0"]').element_by(have.text('Показать')).click()

    @staticmethod
    def check_first_page():
        @allure.step('Проверяем, что автомобили непроданные')
        def should_unsold():
            browser.all('[class="css-z5srlr e162wx9x0"]').should(have.no.text('снят с продажи'))
        should_unsold()
        # @allure.step('Проверяем, что автомобили непроданные')
        # def should_select_year_from(self, year):

        @allure.step('Проверяем, что у автомобилей есть пробег')
        def should_have_mileage():
            browser.all('[class="css-1l9tp44 e162wx9x0"]').by(have.text('км')).should(have.size(20))
        should_have_mileage()

    @staticmethod
    def check_second_page():
        @allure.step('Кликаем на вторую страницу поисковой выдачи')
        def click_on_second_page():
            browser.all('[class="css-1jjais5 ena3a8q0"]').element_by(have.exact_text('2')).click()
        click_on_second_page()

        @allure.step('Проверяем, что автомобили непроданные')
        def should_unsold():
            browser.all('[class="css-z5srlr e162wx9x0"]').should(have.no.text('снят с продажи'))
        should_unsold()

        @allure.step('Проверяем, что у автомобилей есть пробег')
        def should_have_mileage():
            browser.all('[class="css-1w11qyo e1lm3vns0"]').by(have.text('км')).should(have.size(20))
        should_have_mileage()


car_filter = CarFilter()
