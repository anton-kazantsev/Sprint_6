from locators.locator_order_page import OrderLocators
from pages.base_page import PageBase


class OrderPageScooter(PageBase):

    # Кнопки заполнения формы заказа
    def click_button_next(self):
        self.driver.find_element(*OrderLocators.BUTTON_NEXT).click() # Кнопка Далее
    def click_order_final(self):
        self.driver.find_element(*OrderLocators.BUTTON_SCOOTER_ORDER).click()  # Кнопка Заказать

    # Заполнение окна Для кого самокат
    def enter_in_field_name(self, name):
        self.driver.find_element(*OrderLocators.NAME).send_keys(name)   # Ввод имени
    def enter_in_field_family(self, surname):
        self.driver.find_element(*OrderLocators.SURNAME).send_keys(surname)  # Ввод фамилии
    def enter_in_field_address(self, address):
        self.driver.find_element(*OrderLocators.ADDRESS).send_keys(address)  # Ввод адреса
    def enter_in_field_metro(self, station):
        self.driver.find_element(*OrderLocators.STATION_METRO).click()  # Ввод станции метро
        self.driver.find_element(*station).click()
    def enter_in_field_phone(self, number):
        self.driver.find_element(*OrderLocators.NUMBER).send_keys(number)  # Ввод номера телефона

    # Заполнение окна Про аренду
    def enter_in_field_calendar(self, date):
        self.driver.find_element(*OrderLocators.WHEN_TO_BRING).send_keys(date)  # Выбор даты заказа
        self.driver.find_element(*OrderLocators.SELECTED_DAY_CALENDAR).click()
    def enter_in_rental_period(self, rent):
        self.driver.find_element(*OrderLocators.RENTAL_PERIOD).click()  # Выбор срока аренды
        self.driver.find_element(*rent).click()
    def click_checkbox_color(self, color):
        self.driver.find_element(*color).click()  # Выбор цвета
    def enter_comment(self, comment):
        self.driver.find_element(*OrderLocators.COMMENT).send_keys(comment)  # Ввод комментария

    # Всплывающее окно Заказ оформлен
    def successful_order(self):
        return self.driver.find_element(*OrderLocators.CHECK_STATUS).text