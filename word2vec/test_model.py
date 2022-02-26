from gensim.models import KeyedVectors
from utils.reader.csv_reader import CsvReader
from filtering.Filter import Filter

model_name = "./model/w2v_model"


model = KeyedVectors.load(model_name, mmap='r')
vocab = model.wv.key_to_index

test_list = ("주가조작", "곽상도", "이영애", "정우성", "사조영웅전", )

filter = Filter()


for name in test_list:
    is_filter = True
    print(name)
    try:
        res = model.wv.most_similar(name, topn=100)
        if is_filter:
            filter.filter_model(res)
            print("")
        else:
            print(res)

    except KeyError as e:
        print(e)


print(f"Size: {len(vocab)}")
