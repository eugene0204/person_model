import gensim.models

from utils.reader.gen_reader import BigCorpora
from gensim.models import Word2Vec
import logging
import multiprocessing

cpu_count = multiprocessing.cpu_count()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

train_path = "../data/training_data/"
sentences = BigCorpora(train_path, split=True)

# for sent in sentences:
#     pass


#model_path = "./model/w2v_model"
model_path = "./model/null_w2v_model"

model = Word2Vec.load(model_path)
old_size = len(model.wv)

model.build_vocab(sentences, update=True)
model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)
model.save(model_path)

print(f"Before update:{old_size}")
print(f"After update:{len(model.wv)}")



