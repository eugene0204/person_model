from utils.reader.csv_reader import CsvReader
import unittest

class TestNoun(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "../data/noun_data/nouns.csv"
        self.nouns = CsvReader.read_single_column(path=self.path)
        self.josas = ['은', '는', '이', '가', '을', '를', '이']

    def test_isNoun(self):
        word = '아이오아이'
        self.assertTrue(word in self.nouns)

    def test_josa(self):
        word = '러시아는'
        word_ = word[:-1]
        noun_set = set(self.nouns)
        word_set = noun_set.intersection({word})
        word_intersec = noun_set.intersection({word_})

        if not word_set and word_intersec:
            self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()


