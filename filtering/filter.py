from utils.reader.csv_reader import CsvReader
from topic.keyword import Keyword


class Filter:
    def __init__(self):
        self.my_keywords_path = "../data/keyword_data/my_keyword.csv"
        self.crawler_keywords_path = "../data/keyword_data/crawler_keyword.csv"
        self.test_filter_path = "../data/keyword_data/test_keyword.csv"
        self.combined_keywords = self._combine_keywords()

    def _combine_keywords(self) -> set:
        my_keywords = CsvReader.read_mutil_columns(self.my_keywords_path)
        crawler_keywords = CsvReader.read_single_column(self.crawler_keywords_path)
        combined_list = list(set(my_keywords + crawler_keywords))

        for word in combined_list:
            if isinstance(word, str):
                topic = Keyword(keyword=word)
                Keyword.topic_set.add(topic)

        return Keyword.topic_set

    def show_filtered_keywords(self, res):
        keywords = []
        for topic, _ in res:
            topic_ = Keyword(topic)
            keyword = self.combined_keywords.intersection(topic_)
            if keyword:
                keywords.append(keyword)
                if topic_.rootwords:
                    keywords.append(topic_.rootwords)

        if keywords:
            print(keywords)
        else:
            print('"No filtered keywords"')


if __name__ == "__main__":
    pass








