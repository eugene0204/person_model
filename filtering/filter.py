from utils.reader.csv_reader import CsvReader


class Filter:
    def __init__(self):
        self.my_keywords_path = "../data/keyword_data/my_keyword.csv"
        self.crawler_keywords_path = "../data/keyword_data/crawler_keyword.csv"
        self.test_filter_path = "../data/keyword_data/test_keyword.csv"
        self.combined_keywords = self._combine_keywords()

    def _combine_keywords(self):
        my_filter = CsvReader.read_single_column(self.my_keywords_path)
        crawler_filter = CsvReader.read_mutil_columns(self.crawler_keywords_path)

        return list(set(my_filter + crawler_filter))

    def show_filtered_keywords(self, res):
        keywords = []
        for topic, _ in res:
            keyword = {topic} & set(self.combined_keywords)
            if keyword:
                keywords.append(keyword)

        if keywords:
            print(keywords)
        else:
            print('"No filtered keywords"')


if __name__ == "__main__":
    pass








