from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator_order_page import OrderLocators
from data import DaraUrl
import allure


class PageBase:
    @allure.step('Инициализируем driver')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем, пока элемент прогрузится и отобразится')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждем, пока элемент прогрузится и станет кликабельным')
    def wait_and_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждем, пока откроется вторая вкладка')
    def wait_and_open_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Ждем, пока отобразится заголовок страницы Дзен')
    def wait_and_title_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.title_is('Дзен'))

    @allure.step('Пролистывание до искомого элемента')
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Открытие страницы')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Всплывающее окно "Заказ оформлен"')
    def successful_order(self):
        return self.driver.find_element(*OrderLocators.CHECK_STATUS).text

    @allure.step('URL Дзен')
    def url_dzn(self):
        assert DaraUrl.DZEN in self.driver.current_url

    @allure.step('Переход на новое открывшееся окно')
    def move_to_next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('URL Самокат')
    def url_scooter(self):
        assert DaraUrl.SCOOTER in self.driver.current_url