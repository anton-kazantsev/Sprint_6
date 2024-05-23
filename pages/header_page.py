from locators.locator_base_page import LocatorsBasePage
from pages.base_page import PageBase
import allure

class HeaderPage(PageBase):
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