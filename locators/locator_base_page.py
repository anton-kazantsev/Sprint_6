from selenium.webdriver.common.by import By


class LocatorsBasePage:
    # Кнопка Заказать в хэдере
    ORDER_BUTTON_HEAD = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]

    # Лого Самокат
    SCOOTER_LOGO = [By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']"]

    # Лого Яндекс
    YANDEX_LOGO = [By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']"]