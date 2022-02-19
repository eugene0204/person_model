from datetime import date
from datetime import datetime


class Date:
    @staticmethod
    def get_today():
        today = date.today()
        now = datetime.now()
        time_ = now.strftime("%H:%M:%S")
        day = today.strftime("%y%m%d")

        return day + "_" + time_
