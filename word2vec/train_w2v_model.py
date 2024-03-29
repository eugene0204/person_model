from utils.reader.gen_reader import BigCorpora
from gensim.models import Word2Vec
import logging
import multiprocessing

cpu_count = multiprocessing.cpu_count()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

train_path = "../data/training_data/"
train_data = BigCorpora(train_path, split=True)


model_path = "./model/null_w2v_model"

model = Word2Vec(sentences=train_data,
                 vector_size=300,
                 sg=1,
                 window=7,
                 min_count=1,
                 epochs=10,
                 hs=1,
                 workers=cpu_count)

model.save(model_path)
print(f"w2v size: {len(model.wv)}")


