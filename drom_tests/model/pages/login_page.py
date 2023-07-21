import os
import allure
from selene.support.shared import browser
from selene import browser, have, be, command


class LoginPage:

    @allure.step('Открываем страницу drom')
    def given_opened(self):
        browser.open('https://auto.drom.ru/')

    @allure.step('Клипаем по кнопке "Вход и регистрация"')
    def click_to_authorization_button(self):
        browser.element('[class="css-1h9spzo e1k6fwrt0"]').click()

    @allure.step('Вводим логин')
    def type_login(self):
        browser.element('#sign').type(os.getenv('login'))

    @allure.step('Вводим пароль')
    def type_password(self):
        browser.element('[id="password"]').type(os.getenv('password'))

    @allure.step('Кликаем на кнопку с авторизацией')
    def click_to_sign_button(self):
        browser.element('#signbutton').click()

    @allure.step('Добавляем одно авто в избранное')
    def add_car_to_favorites(self):
        browser.all('[class="css-1rozdag"]').element(0).click()

    @allure.step('Переходим в избранное')
    def click_to_user_favorites_button(self):
        browser.all('[title="Избранное"]').element(1).click()
        browser.driver.refresh()

    @allure.step('Проверяем, что в избранное добавлен один автомобиль')
    def should_have_added_favorite_car(self):
        browser.all('[class="bull-item-content"]').should(have.size(1))


login_page = LoginPage()