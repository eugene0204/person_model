from datetime import date


class Date:
    @staticmethod
    def get_today():
        today = date.today()
        day = today.strftime("%y%m%d")

        return day
