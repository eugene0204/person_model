from gensim.models import KeyedVectors
from utils.hangul.hangul_parser import HangulParser
import numpy as np


class Similarity:
    def __init__(self, model_path):
        self.model = KeyedVectors.load(model_path)
        self.dim = 300

    def _get_sum_vector(self, sentence: str):
        sum_vector = np.zeros(self.dim)
        hangul = HangulParser.get_hangul(sentence)
        count = 0

        for word in hangul:
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

    test_str = "어제 저의 1분은 故 이예람 중사를 기억하는 1분이었습니다."
    res = sim.get_most_sim(test_str)
    print(res)











