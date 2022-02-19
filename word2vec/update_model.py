import gensim.models

from utils.reader.gen_reader import BigSentence
from gensim.models import Word2Vec
import logging
import multiprocessing

cpu_count = multiprocessing.cpu_count()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

train_path = "../data/training_data/"
sentences = BigSentence(train_path, split=True)

# for sent in sentences:
#     pass


model_path = "./model/w2v_model"
model = Word2Vec.load(model_path)

print(f"Before update:{len(model.wv)}")

model.build_vocab(sentences, update=True)
model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)
model.save(model_path)

print(f"After update:{len(model.wv)}")



