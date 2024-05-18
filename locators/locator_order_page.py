from selenium.webdriver.common.by import By


class OrderLocators:

    # Кнопка окна Для кого самокат
    BUTTON_NEXT = [By.XPATH, ".//button[text() = 'Далее']"]

    # Страница Для кого самокат
    NAME = [By.XPATH, ".//input[@placeholder = '* Имя']"] # Ввод имени
    SURNAME = [By.XPATH, ".//input[@placeholder = '* Фамилия']"] # Ввод фамилии
    ADDRESS = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"] # Ввод адреса
    STATION_METRO = [By.XPATH, ".//input[@placeholder = '* Станция метро']"] # Окно выбора станции
    NUMBER = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"] # Ввод номера телефона

    # Выбор станции
    STATION_SOKOLNIKI = [By.XPATH, ".//li[@data-index = 3]"]
    STATION_LUBYANKA = [By.XPATH, ".//li[@data-index = 1]"]

    # Кнопки окна Про аренду
    BUTTON_SCOOTER_ORDER = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"] # Кнопка Заказать
    BUTTON_YES = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Да']"] # Кнопка Да окна оформления заказа

    # Страница Про аренду
    WHEN_TO_BRING = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"] # Когда привезти самокат
    SELECTED_DAY_CALENDAR = [By.XPATH, ".//div[contains(@class, 'react-datepicker__day--selected')]"] # Когда привезти самокат
    RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-placeholder"] # Срок аренды
    COMMENT = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"] # Комментарий для курьера

    # Сроки аренды
    RENT_FOR_ONE_DAY = [By.XPATH, ".//div[text() = 'сутки']"]
    RENT_FOR_TWO_DAYS = [By.XPATH, ".//div[text() = 'двое суток']"]

    # Цвета
    COLOR_BLACK = [By.XPATH, ".//label[@for= 'black']"]  # цвет "Чёрный жемчуг"
    COLOR_GREY = [By.XPATH, ".//label[@for= 'grey']"]  # цвет "Серая безысходность"

    # Кнопка "Посмотреть статус"
    CHECK_STATUS = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']/button[text() = 'Посмотреть статус']"]

