import unittest
from custom.keyword import Keyword


class TestKeyword(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_repr(self):
        keyword = Keyword("더스틴 니퍼트")
        print(repr(keyword))

    def test_equal(self):
        keyword1 = Keyword("이응준")
        keyword2 = Keyword("이응준")

        self.assertTrue(keyword1 == keyword2)

    def test_equal_sub(self):
        topic1 = Keyword('더스틴 니퍼트')
        topic2 = Keyword('니퍼트')

        self.assertTrue(topic2 == topic1)


    def test_hash(self):
        keyword1 = Keyword("이응준")
        keyword2 = Keyword("이응준")
        size = len(set([keyword1, keyword2]))

        self.assertTrue(size == 1)

    def test_intersection(self):
        topic1 = Keyword('더스틴 니퍼트')
        topic2 = Keyword('김태우 (1989년)')
        topic3 = Keyword('더스틴 니퍼트')

        topic_set = {topic2, topic1}

        inter = topic_set.intersection(topic3)

        self.assertTrue(len(inter) == 1)

    def test_sub_inter(self):
        topic1 = Keyword('더스틴 니퍼트')
        topic2 = Keyword('김태우 (1989년)')
        topic3 = Keyword('더스틴')

        topic_set = {topic1, topic2}

        inter = topic_set.intersection(topic3)
        print(inter)

        self.assertTrue(len(inter) == 1)


if __name__ == "__main__":
    unittest.main()


