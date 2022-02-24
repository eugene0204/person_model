from gensim.models import KeyedVectors
from utils.reader.csv_reader import CsvReader

model_name = "./model/w2v_model"
filter_data_path = "../data/filter/my_filter.csv"


filter = CsvReader.read_file(filter_data_path, header=True)
filter = set(filter)

model = KeyedVectors.load(model_name, mmap='r')
vocab = model.wv.key_to_index

test_list = ("주가조작", "곽상도", "이영애", "정우성", "사조영웅전", )


def filtering(res):
    for topic, _ in res:
        common = {topic} & filter
        if common:
            print(common, end=" ")

for name in test_list:
    filter = False
    print(name)
    try:
        res = model.wv.most_similar(name, topn=100)
        if filter:
            filtering(res)
            print("")
        else:
            print(res)

    except KeyError as e:
        print(e)


print(f"Size: {len(vocab)}")
