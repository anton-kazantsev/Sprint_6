from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator_base_page import LocatorsBasePage
from locators.locator_main_page import QuestionLocators
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

    # Нажатие на маленькую кнопку Заказать в хэдере
    @allure.step('Нажатие "Заказать" в хэд')
    def click_button_order_in_header(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_HEAD).click()

    @allure.step('Нажатие на текст Самокат в хэдере')
    def click_logo_scooter(self):
        self.driver.find_element(*LocatorsBasePage.SCOOTER_LOGO).click()

    @allure.step('Нажатие на текст Яндекс в хэдере')
    def click_logo_yandex(self):
        self.driver.find_element(*LocatorsBasePage.YANDEX_LOGO).click()

    @allure.step('Открытие страницы')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Открытие списка с вопросами')
    def open_drop_list(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Сравнение текста в выпадающем окне')
    def text_comparison_drop_list(self, answer):
        return self.driver.find_element(*answer).text

    @allure.step('Нажатие большой кнопки Заказать на главном окне')
    def click_big_button_order(self):
        self.driver.find_element(*QuestionLocators.BIG_BUTTON_ORDER).click()

    # Шаг подтверждение заказа
    @allure.step('Нажатие кнопки Да в окне подтверждения оформления заказа')
    def click_order_confirmation(self):
        self.driver.find_element(*OrderLocators.BUTTON_YES).click()

    # Кнопки заполнения формы заказа
    @allure.step('Нажимаем кнопку "Далее" в форме заказа')
    def click_button_next(self):
        self.driver.find_element(*OrderLocators.BUTTON_NEXT).click()

    @allure.step('Нажимаем кнопку "Заказать" в форме заказа')
    def click_order_final(self):
        self.driver.find_element(*OrderLocators.BUTTON_SCOOTER_ORDER).click()

    # Заполнение окна Для кого самокат
    @allure.step('Вводим Имя')
    def enter_in_field_name(self, name):
        self.driver.find_element(*OrderLocators.NAME).send_keys(name)

    @allure.step('Вводим Фамилию')
    def enter_in_field_family(self, surname):
        self.driver.find_element(*OrderLocators.SURNAME).send_keys(surname)

    @allure.step('Вводим Адрес')
    def enter_in_field_address(self, address):
        self.driver.find_element(*OrderLocators.ADDRESS).send_keys(address)

    @allure.step('Выбираем станцию')
    def enter_in_field_metro(self, station):
        self.driver.find_element(*OrderLocators.STATION_METRO).click()
        self.driver.find_element(*station).click()

    @allure.step('Вводим Номер телефона')
    def enter_in_field_phone(self, number):
        self.driver.find_element(*OrderLocators.NUMBER).send_keys(number)

    # Заполнение окна Про аренду
    @allure.step('Выбираем дату заказа')
    def enter_in_field_calendar(self, date):
        self.driver.find_element(*OrderLocators.WHEN_TO_BRING).send_keys(date)
        self.driver.find_element(*OrderLocators.SELECTED_DAY_CALENDAR).click()

    @allure.step('Выбираем срок аренды')
    def enter_in_rental_period(self, rent):
        self.driver.find_element(*OrderLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*rent).click()

    @allure.step('Выбираем цвет самоката')
    def click_checkbox_color(self, color):
        self.driver.find_element(*color).click()

    @allure.step('Вводим комментарий')
    def enter_comment(self, comment):
        self.driver.find_element(*OrderLocators.COMMENT).send_keys(comment)

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