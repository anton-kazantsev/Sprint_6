from datetime import timedelta
from datetime import datetime


class DataCalendar:
    @classmethod
    def get_tomorrow_date(cls):
        tomorrow_date = datetime.today() + timedelta(days=1)
        return tomorrow_date.date().strftime("%d.%m.%Y")

    @classmethod
    def get_next_week_date(cls):
        tomorrow_date = datetime.today() + timedelta(days=7)
        return tomorrow_date.date().strftime("%d.%m.%Y")