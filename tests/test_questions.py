import pytest
from pages.main_page import MainPageScooter
from locators.locator_main_page import QuestionLocators
from data import TextAnswerDropList
from data import DaraUrl
from conftest import driver
import allure


class TestExpandingDropList:
    @allure.title('Нажатие на списки для проверки Вопросов о главном')
    @allure.description('Текст ответов открывается при нажатии на стрелку')
    @pytest.mark.parametrize(
        'question,answer,text',
        [
            [QuestionLocators.HOW_MUCH, QuestionLocators.HOW_MUCH_ANSWER, TextAnswerDropList.text_how_much],
            [QuestionLocators.SEVERAL_SCOOTERS, QuestionLocators.SEVERAL_SCOOTER_ANSWER, TextAnswerDropList.text_want_scooters],
            [QuestionLocators.TIMES, QuestionLocators.TIMES_ANSWER, TextAnswerDropList.text_how_rental],
            [QuestionLocators.ORDER_FOR_TODAY, QuestionLocators.ORDER_FOR_TODAY_ANSWER, TextAnswerDropList.text_possible_order],
            [QuestionLocators.EXTEND_OF_REFUND, QuestionLocators.EXTEND_OR_REFUND_ANSWER, TextAnswerDropList.text_extend_or_return],
            [QuestionLocators.CHARGING, QuestionLocators.CHARGING_ANSWER, TextAnswerDropList.text_bringing_charges],
            [QuestionLocators.CANCEL, QuestionLocators.CANSEL_ANSWER, TextAnswerDropList.text_cansel],
            [QuestionLocators.BEYOND_THE_MKAD, QuestionLocators.BEYOND_THE_MKAD_ANSWER, TextAnswerDropList.text_far_life]
        ]
    )
    def test_expanding_drop_list(self, driver, question, answer, text):
        question_answer = MainPageScooter(driver)
        question_answer.open_page(DaraUrl.SCOOTER)
        answer_text = question_answer.expanding_list(question, answer)
        assert answer_text == text