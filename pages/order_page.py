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