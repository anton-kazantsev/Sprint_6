from selenium.webdriver.common.by import By


class QuestionLocators:

    # Большая кнопка Заказать
    BIG_BUTTON_ORDER = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]

    # Важные вопросы
    QUESTIONS_ABOUT_IMPORTANT = [By.XPATH, ".//div[text() = 'Вопросы о важном']"]

    # Вопросы выпадающего списка "Вопросы о главном"
    HOW_MUCH = [By.ID, 'accordion__heading-0']  # вопрос "Сколько это стоит? И как оплатить?"
    SEVERAL_SCOOTERS = [By.ID, 'accordion__heading-1']  # вопрос "Хочу сразу несколько самокатов! Так можно?"
    TIMES = [By.ID, 'accordion__heading-2']  # вопрос "Как рассчитывается время аренды?"
    ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']  # вопрос "Можно ли заказать самокат прямо на сегодня?"
    EXTEND_OF_REFUND = [By.ID, 'accordion__heading-4']  # вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    CHARGING = [By.ID, 'accordion__heading-5']  # вопрос "Вы привозите зарядку вместе с самокатом?"
    CANCEL = [By.ID, 'accordion__heading-6']  # вопрос "Можно ли отменить заказ?"
    BEYOND_THE_MKAD = [By.ID, 'accordion__heading-7']  # вопрос "Я живу за МКАДом, привезёте?"

    # Текст в выпадающих списках
    HOW_MUCH_ANSWER = [By.ID, 'accordion__panel-0']  # ответ 1
    SEVERAL_SCOOTER_ANSWER = [By.ID, 'accordion__panel-1']  # ответ 2
    TIMES_ANSWER = [By.ID, 'accordion__panel-2']  # ответ 3
    ORDER_FOR_TODAY_ANSWER = [By.ID, 'accordion__panel-3']  # ответ 4
    EXTEND_OR_REFUND_ANSWER = [By.ID, 'accordion__panel-4']  # ответ 5
    CHARGING_ANSWER = [By.ID, 'accordion__panel-5']  # ответ 6
    CANSEL_ANSWER = [By.ID, 'accordion__panel-6']  # ответ 7
    BEYOND_THE_MKAD_ANSWER = [By.ID, 'accordion__panel-7']  # ответ 8