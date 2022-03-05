from gensim.models import KeyedVectors
from utils.reader.csv_reader import CsvReader
from filtering.Filter import Filter

model_name = "./model/null_w2v_model"

model = KeyedVectors.load(model_name, mmap='r')
vocab = model.wv.key_to_index

test_list = ("알파고", "짜장면", "짬뽕", "문재인", "이재명", "윤석열", "심상정", "안철수")

filter = Filter()

for name in test_list:
    print(name)
    try:
        res = model.wv.most_similar(name, topn=100)
        filter.filter_model(res)
        print("")
        print(res)

    except KeyError as e:
        print(e)
