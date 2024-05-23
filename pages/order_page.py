from locators.locator_order_page import OrderLocators
from pages.base_page import PageBase
import allure


class OrderPageScooter(PageBase):

    @allure.step(
        'Заполнение полей окна: Для кого самокат и нажатие кнопки Далее')
    def first_step_order(self, name, surname, address, station, number):
        self.enter_in_field_name(name)
        self.enter_in_field_family(surname)
        self.enter_in_field_address(address)
        self.enter_in_field_metro(station)
        self.enter_in_field_phone(number)
        self.click_button_next()
        self.wait_and_find_element(OrderLocators.BUTTON_SCOOTER_ORDER)

    # Шаг Про аренду
    @allure.step('Заполнение полей окна: Про аренду и нажатие кнопки Заказать')
    def second_step_order(self, date, rent, color, comment):
        self.enter_in_field_calendar(date)
        self.enter_in_rental_period(rent)
        self.click_checkbox_color(color)
        self.enter_comment(comment)
        self.click_order_final()

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
