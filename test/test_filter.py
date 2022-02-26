from utils.reader.csv_reader import CsvReader
import unittest


class FilterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_filter_path = "../data/filter/my_filter.csv"
        self.crawler_filter_path = "../data/filter/crawler_filter.csv"
        self.test_filter_path = "../data/filter/test_filter.csv"

    def test_combine_filters(self):
        my_filter = CsvReader.read_file(self.my_filter_path)
        crawler_filter = CsvReader.read_file(self.crawler_filter_path)
        total_len = len(set(my_filter)) + len(set(crawler_filter))

        self.assertTrue(len(my_filter + crawler_filter) == total_len)


if __name__ == "__main__":
    unittest.main()

