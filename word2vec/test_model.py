from gensim.models import KeyedVectors
from utils.reader.csv_reader import CsvReader
from filtering.filter import Filter


class TestModel:
    def __init__(self):
        self.model_name = "./model/null_w2v_model"
        self.model = KeyedVectors.load(self.model_name, mmap='r')
        self.vocab = self.model.wv.key_to_index
        self.test_list = ("짜장면", "짬뽕", "문재인", "이재명", "윤석열", "심상정", "안철수")
        self.filter = Filter()

    def show_test_list(self):
        for name in self.test_list:
            print(name)
            try:
                res = self.model.wv.most_similar(name, topn=100)
                self.filter.show_filtered_keywords(res)
                print(res)

            except KeyError as e:
                print(e)

    def show_most_similar(self, keyword):
        try:
            res = self.model.wv.most_similar(keyword, topn=100)
            self.filter.show_filtered_keywords(res)
            print(res)
            return

        except KeyError as e:
            print(e)



if __name__ == "__main__":
    model = TestModel()
    while True:
        keyword = input(">> ")
        if keyword == "exit":
            break
        elif keyword == "show":
            model.show_test_list()
        else:
            model.show_most_similar(keyword)



