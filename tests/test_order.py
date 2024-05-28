from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from pages.header_page import HeaderPage
from conftest import driver
import allure
from data import DataForOrder
from data import DaraUrl


class TestOrderScooter:

    @allure.title('Проверяем возможность заказа на кнопку Заказать в хэдере')
    @allure.description('Позитивный сценарий создания заказа аренды самоката через маленькую кнопку заказать')
    def test_order_button_in_header(self, driver):
        search_button_order = HeaderPage(driver)
        test_order_scooter = OrderPageScooter(driver)
        search_button_order.open_page(DaraUrl.SCOOTER)
        search_button_order.click_button_order_in_header()
        test_order_scooter.first_step_order(DataForOrder.data_order_1['name'], DataForOrder.data_order_1['surname'],
                                            DataForOrder.data_order_1['address'], DataForOrder.data_order_1['station'],
                                            DataForOrder.data_order_1['number'])
        test_order_scooter.second_step_order(DataForOrder.data_order_1['date'], DataForOrder.data_order_1['rent'],
                                             DataForOrder.data_order_1['color'], DataForOrder.data_order_1['comment'])
        test_order_scooter.click_order_confirmation()
        head_successful_order = test_order_scooter.successful_order()
        assert head_successful_order == 'Посмотреть статус'

    @allure.title('Проверяем возможность заказа на большую кнопку Заказать в нижней части главного экрана')
    @allure.description('Позитивный сценарий создания заказа аренды самоката через большую кнопку Заказать')
    def test_order_big_button(self, driver):
        search_button_order = MainPageScooter(driver)
        test_order_scooter = OrderPageScooter(driver)
        search_button_order.open_page(DaraUrl.SCOOTER)
        search_button_order.button_order_in_page()
        test_order_scooter.first_step_order(DataForOrder.data_order_2['name'], DataForOrder.data_order_2['surname'],
                                           DataForOrder.data_order_2['address'], DataForOrder.data_order_2['station'],
                                           DataForOrder.data_order_2['number'])
        test_order_scooter.second_step_order(DataForOrder.data_order_2['date'], DataForOrder.data_order_2['rent'],
                                            DataForOrder.data_order_2['color'], DataForOrder.data_order_2['comment'])
        test_order_scooter.click_order_confirmation()
        head_successful_order = test_order_scooter.successful_order()
        assert head_successful_order == 'Посмотреть статус'

    @allure.title('Проверяем возможность перехода на главную страницу через нажатие на надпись Самокат')
    @allure.description('При нажатие на текст Самокат происходит переход на главную страницу')
    def test_go_to_main_page(self, driver):
        test_order_scooter = HeaderPage(driver)
        test_order_scooter.open_page(DaraUrl.SCOOTER + 'order')
        test_order_scooter.click_logo_scooter()
        test_order_scooter.url_scooter()

    @allure.title('Проверяем возможность перехода на страницу Дзен через нажатие на текст Яндекс')
    @allure.description('При нажатие на текст Яндекс происходит переход на страницу Дзен')
    def test_go_to_dzen(self, driver):
        test_order_scooter = HeaderPage(driver)
        test_order_scooter.open_page(DaraUrl.SCOOTER)
        test_order_scooter.click_logo_yandex()
        test_order_scooter.wait_and_open_tab()
        test_order_scooter.move_to_next_window()
        test_order_scooter.wait_and_title_tab()
        test_order_scooter.url_dzn()