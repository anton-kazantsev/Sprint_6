from locators.locator_main_page import QuestionLocators
from pages.base_page import PageBase
import allure


class MainPageScooter(PageBase):

    @allure.step('Нажатие на раздел Вопроса о главном')
    def expanding_list(self, question, answer):
        self.scroll_element(QuestionLocators.QUESTIONS_ABOUT_IMPORTANT)
        self.wait_and_clickable(question)
        self.open_drop_list(question)
        self.wait_and_find_element(answer)
        return self.text_comparison_drop_list(answer)

    # Нажатие на большую кнопку Заказать
    @allure.step('Пролистываем окно и нажимаем на большую кнопку Заказать')
    def button_order_in_page(self):
        self.scroll_element(QuestionLocators.BIG_BUTTON_ORDER)
        self.wait_and_find_element(QuestionLocators.BIG_BUTTON_ORDER)
        self.click_big_button_order()