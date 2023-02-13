import unittest
import re
from pre_process.regex.regex_parser import RegexParser
from collections import Counter



class HangulTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = RegexParser

    def test_get_hangul(self):
        test_str1 = "아 피자 먹고 싶어!!"
        test_str2 = "아 pizza 먹고 싶어!@#@$%3q322!!"

        expected_1 = ['아', '피자', '먹고', '싶어']
        expected_2 = ['아', '먹고', '싶어']

        hangul_1 = RegexParser.get_hangul(test_str1)
        self.assertTrue(len(hangul_1) == 4)
        self.assertTrue(Counter(hangul_1) == Counter(expected_1))

        hangul_2 = RegexParser.get_hangul(test_str2)
        self.assertTrue(len(hangul_2) == 3)
        self.assertTrue(Counter(hangul_2) == Counter(expected_2))

    def test_get_clean_sent(self):
        RT = "RT"
        test_str1 = \
            "RT @supio0204 미국과 russia는 2022년 세계3차대전을 준비 하고 있다!! RT거거 ABC 30% http://www.my.com"
        test_str1_sub ="@supio0204 미국과 russia는 2022년 세계3차대전을 준비 하고 있다!! RT거거 ABC 30% http://www.my.com"
        exptected = ['미국과', 'russia는', '2022년', '세계3차대전을', '준비', '하고', '있다', 'RT거거', 'ABC', '30%']


        split = test_str1.split()
        if RT == split[0]:
            split = split[1:]
            test_str1_ = " ".join(split)
            self.assertTrue(test_str1_sub == test_str1_)

        url_pattern = r"(http\S+)"
        test_str1_sub = re.sub(url_pattern, "", test_str1_sub)

        id_pattern = r"@\S+"
        test_str1_sub = re.sub(id_pattern, "", test_str1_sub)

        pattern = '[\uAC00-\uD7AF\d\u0041-\u005A\u0061-\u007A\u0025]+'
        test_str1_sub = re.findall(pattern, test_str1_sub)
        print(test_str1_sub)
        self.assertTrue(exptected == test_str1_sub)




if __name__ == "__main__":
    unittest.main()
