from gensim.models import KeyedVectors

model_name = "./model/w2v_model"
model = KeyedVectors.load(model_name, mmap='r')
vocab = model.wv.key_to_index
print(f"Size: {len(vocab)}")
test_list = ("짜장면", "짬뽕", "피자", "문재인")

for name in test_list:
    print(name)
    try:
        print(model.wv.most_similar(name, topn=10))
    except KeyError as e:
        print(e)