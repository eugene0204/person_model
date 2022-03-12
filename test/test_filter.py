from utils.reader.csv_reader import CsvReader
from topic.keyword import Keyword
from filtering.filter import Filter
import unittest
import pandas as pd


class FilterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_keywords_path = "../data/keyword_data/my_keyword.csv"
        self.crawler_keywords_path = "../data/keyword_data/crawler_keyword.csv"
        self.test_words_path = "../data/keyword_data/test_keyword.csv"

    def test_combine_filters(self):
        my_filter = CsvReader.read_single_column(self.my_keywords_path)
        crawler_filter = CsvReader.read_single_column(self.crawler_keywords_path)
        total_len = len(set(my_filter)) + len(set(crawler_filter))

        self.assertTrue(len(my_filter + crawler_filter) == total_len)

    def test_read_multiple_column(self):
        my_list = []
        res = pd.read_csv(self.test_words_path)
        for col in res:
            my_list.extend(res[col].to_list())

        self.assertTrue(len(my_list) == 10)

    def test_sub_match(self):
        topic1 = Keyword('더스틴 니퍼트')
        topic2 = Keyword('김태우 (1989년)')
        topic3 = Keyword('더스틴 니퍼트')

        filter_set = {topic1, topic2}

        if filter_set.intersection(topic3):
            print("find")
        else:
            print("no")






if __name__ == "__main__":
    unittest.main()

