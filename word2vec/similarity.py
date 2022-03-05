from gensim.models import KeyedVectors
from utils.regex.regex_parser import RegexParser
import numpy as np


class Similarity:
    def __init__(self, model_path):
        self.model = KeyedVectors.load(model_path)
        self.dim = 300

    def _get_sum_vector(self, sentence: str):
        sum_vector = np.zeros(self.dim)
        clean_sent = RegexParser.get_clean_sentence(sentence)

        print(f"{clean_sent}")

        count = 0

        for word in clean_sent:
            try:
                sum_vector = np.add(sum_vector, self.model.wv[word])
                count += 1
            except KeyError as e:
                print(e)

        return sum_vector, count

    def _get_mean_vector(self, sum_vec: np.ndarray, count):
        if count != 0:
            mean_vec = np.divide(sum_vec, count)
        else:
            mean_vec = np.zeros(self.dim)

        return mean_vec

    def get_most_sim(self, sentence: str):
        _sum_vector , _count = self._get_sum_vector(sentence)
        mean_vec = self._get_mean_vector(_sum_vector, _count)

        most_sim = self.model.wv.most_similar(mean_vec, topn=10)

        return most_sim

if __name__ == "__main__":
    model_path = '../word2vec/model/w2v_model'
    sim = Similarity(model_path)

    test_str = "다시 상기시켜보면... 러시아는 내일부터 믿을게 골드랑 위안화 밖에 없음."
    res = sim.get_most_sim(test_str)
    print(res)











