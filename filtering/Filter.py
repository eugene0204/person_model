from utils.reader.csv_reader import CsvReader


class Filter:
    def __init__(self):
        self.my_filter_path = "../data/filter_data/my_filter.csv"
        self.crawler_filter_path = "../data/filter_data/crawler_filter.csv"
        self.test_filter_path = "../data/filter_data/test_filter.csv"

    def combine_filters(self):
        my_filter = CsvReader.read_file(self.my_filter_path)
        crawler_filter = CsvReader.read_file(self.crawler_filter_path)

        return list(set(my_filter + crawler_filter))

    def filter_model(self, res):
        filter = self.combine_filters()

        for topic, _ in res:
            common = {topic} & set(filter)
            if common:
                print(common, end=" ")






