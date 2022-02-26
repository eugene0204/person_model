import re


class HangulParser:

    @staticmethod
    def get_hangul(sentence: str):
        hangul = re.findall(u'[\uAC00-\uD7A3]+', sentence)

        return hangul