import unittest
import csv
from collections import Counter

class WriterText(unittest.TestCase):
    def setUp(self) -> None:
        self.test_lst = ['우크라이나', '우크라이나러시아전쟁', '엘든링', '토트넘', 'CNN', 'LCK', '나토', 'EPL', '맨유', '포켓몬빵']
        self.path = "../data/filter/test_filter.csv"

    def test_csv_writer(self):
        with open(self.path, 'w') as file:
            writer = csv.writer(file)
            for sent in self.test_lst:
                self.assertTrue(isinstance(sent, str))
                writer.writerow([sent])

        res = []
        with open(self.path, "r") as file:
            reader = csv.reader(file)
            for sent in reader:
                self.assertTrue(isinstance(sent[0], str))
                res.append(sent[0])

        self.assertTrue(Counter(res) == Counter(self.test_lst))


if __name__ == "__main__":
    unittest.main()
