import unittest
from utils.hangul.hangul_parser import HangulParser

class HangulTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = HangulParser

    def test_get_hangul(self):
        test_str1 = "아 피자 먹고 싶어!!"
        test_str2 = "아 pizza 먹고 싶어!@#@$%3q322!!"

        hangul_1 = HangulParser.get_hangul(test_str1)
        self.assertTrue(len(hangul_1) == 4)

        hangul_2 = HangulParser.get_hangul(test_str2)
        self.assertTrue(len(hangul_2) == 3)


if __name__ == "__main__":
    unittest.main()
