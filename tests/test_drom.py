import allure

from drom_tests.model.pages.car_filter_script import car_filter_script
from drom_tests.model.pages.car_filter import car_filter
from drom_tests.model.pages.login_page import login_page


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Настройка фильтра для выдачи')
@allure.link('', name='Testing')
def test_car_filter(test_browser_configuration):
    # GIVEN
    car_filter.given_opened()
    # WHEN
    car_filter.select_brand('Toyota')
    car_filter.select_model('Harrier')
    car_filter.select_type_of_fuel('Гибрид')
    car_filter.select_year_from('2007')
    car_filter.select_checkbox_unsold()
    car_filter.show_advanced_search()
    car_filter.scroll_to_mileage()
    car_filter.set_mileage_from('1')
    car_filter.show_results()

    # THEN
    car_filter.check_first_page()
    car_filter.check_second_page()


def test_add_to_favorites(test_browser_configuration, clear_test_artifacts):
    # GIVEN
    login_page.given_opened()
    # WHEN
    login_page.click_to_authorization_button()
    login_page.type_login()
    login_page.type_password()
    login_page.click_to_sign_button()
    login_page.add_car_to_favorites()
    login_page.click_to_user_favorites_button()

    # THEN
    login_page.should_have_added_favorite_car()


def test_car_filter_script():
    car_filter_script.given_opened()
    car_filter_script.select_region('Приморский край')
    car_filter_script.show_amounts_of_brands()
