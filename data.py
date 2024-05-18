from locators.locator_order_page import OrderLocators
from helpers import DataCalendar


class TextAnswerDropList:
    text_how_much = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_want_scooters = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    text_how_rental = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_possible_order = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    text_extend_or_return = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    text_bringing_charges = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    text_cansel = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    text_far_life = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class DataForOrder:
    data_order_1 = {
        'name': 'Антон',
        'surname': 'Казанцев',
        'address': 'г. Химки',
        'station': OrderLocators.STATION_SOKOLNIKI,
        'number': '+79999998199',
        'date': DataCalendar.get_tomorrow_date(),
        'rent': OrderLocators.RENT_FOR_ONE_DAY,
        'color': OrderLocators.COLOR_GREY,
        'comment': 'Запрягай коней'
    }

    data_order_2 = {
        'name': 'Ариана',
        'surname': 'Грант',
        'address': 'г. Москва',
        'station': OrderLocators.STATION_LUBYANKA,
        'number': '+79991339999',
        'date': DataCalendar.get_next_week_date(),
        'rent': OrderLocators.RENT_FOR_TWO_DAYS,
        'color': OrderLocators.COLOR_BLACK,
        'comment': 'Вези извозчик'
    }


class DaraUrl:
    SCOOTER = 'https://qa-scooter.praktikum-services.ru/'
    DZEN = 'https://dzen.ru/'