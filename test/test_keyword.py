import unittest
from topic.keyword import Keyword


class TestKeyword(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_repr(self):
        keyword = Keyword("더스틴 니퍼트")
        self.assertTrue(repr(keyword) == "더스틴 니퍼트")

    def test_equal(self):
        keyword1 = Keyword("이응준")
        keyword2 = Keyword("이응준")

        self.assertTrue(keyword1 == keyword2)

    def test_equal_sub(self):
        topic1 = Keyword('더스틴 니퍼트')
        topic2 = Keyword('니퍼트')

        self.assertFalse(topic2 == topic1)


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
        topic4 = Keyword('니퍼트')
        topic5 = Keyword('더스틴 아파트')

        Keyword.word_set.add(topic1)
        Keyword.word_set.add(topic2)
        Keyword.word_set.add(topic5)

        inter = Keyword.word_set.intersection(topic3)
        topic = next(iter(inter))

        self.assertTrue(len(inter) == 1)
        self.assertTrue(topic1.keyword or topic5.keyword in topic.rootwords)


if __name__ == "__main__":
    unittest.main()


