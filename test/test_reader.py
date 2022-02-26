import unittest
from utils.reader.csv_reader import CsvReader

from collections import Counter

class ReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.filter_path = "../data/filter/test_filter.csv"
        self.test_lst = ['우크라이나', '우크라이나러시아전쟁', '엘든링', '토트넘', 'CNN', 'LCK', '나토', 'EPL', '맨유', '포켓몬빵']

    def test_read_csv_file(self):
        res = CsvReader.read_file(self.filter_path)
        self.assertTrue(Counter(self.test_lst) == Counter(res))

if __name__ == "__main__":
    unittest.main()
