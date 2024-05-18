from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator_base_page import LocatorsBasePage
import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    # Ждем, пока элемент прогрузится и отобразится
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Ждем, пока элемент прогрузится и станет кликабельным
    def wait_and_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    # Ждем, пока откроется вторая вкладка
    def wait_and_open_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))

    # ждём, пока отобразится заголовок страницы Дзен
    def wait_and_title_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.title_is('Дзен'))

    # Пролистывание до искомого элемента
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Нажатие на маленькую кнопку Заказать в хэдере
    @allure.step('Нажатие "Заказать" в хэд')
    def click_button_order_in_header(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_HEAD).click()

    # Нажатие на текст Самокат в хэдере
    def click_logo_scooter(self):
        self.driver.find_element(*LocatorsBasePage.SCOOTER_LOGO).click()

    # Нажатие на текст Яндекс в хэдере
    def click_logo_yandex(self):
        self.driver.find_element(*LocatorsBasePage.YANDEX_LOGO).click()

    # Открытие страницы
    def open_page(self, url):
        self.driver.get(url)