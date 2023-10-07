import heapq
import re
import time
import string

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:\\ATProject\\Drom\\chromedriver.exe')


class CarFilterScript:
    def given_opened(self):
        driver.maximize_window()
        driver.get('https://auto.drom.ru/')

    def select_region(self, region):
        choose_region_button = driver.find_element(By.CSS_SELECTOR, '[data-ga-stats-name="geoOverCity"]')
        choose_region_button.click()
        time.sleep(2)
        region_input = driver.find_element(By.XPATH, "//input[@placeholder='поиск города, региона']")
        region_input.send_keys(region)
        region_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def show_amounts_of_brands(self):
        show_all = driver.find_element(By.CSS_SELECTOR, '[class="css-atyutb e1cj4jfp2"]')
        show_all.click()
        list_elements = driver.find_elements(By.CSS_SELECTOR, '[class="css-yhyz6a e4ojbx44"]')

        new_dict = {}
        for i in list_elements:
            brand = i.text.rstrip(string.digits).strip()
            amount = int(re.sub("[^0-9]", "", i.text))
            new_dict[brand] = amount

        sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))
        count = 0
        for i in sorted_dict:
            if count == 0:
                print(f"\n|Фирма|Количество объявлений|")
            if count < 20:
                print(f"|{i}|{sorted_dict[i]}|")
            count += 1

        driver.close()


car_filter_script = CarFilterScript()
