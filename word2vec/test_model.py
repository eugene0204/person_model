from gensim.models import KeyedVectors
from utils.reader.csv_reader import CsvReader

model_name = "./model/w2v_model"
filter_data_path = "../data/filter/filter.csv"


filter = CsvReader.read_file(filter_data_path, header=True)
filter = set(filter)

model = KeyedVectors.load(model_name, mmap='r')
vocab = model.wv.key_to_index

test_list = ("이만기", "도이치모터스", "아들", "무당", "대장동", )


def filtering(res):
    for topic, _ in res:
        common = {topic} & filter
        if common:
            print(common, end=" ")

for name in test_list:
    print(name)
    try:
        res = model.wv.most_similar(name, topn=100)
        filtering(res)
        print("")

    except KeyError as e:
        print(e)


print(f"Size: {len(vocab)}")
