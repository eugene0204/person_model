from gensim.models import KeyedVectors
from pre_process.regex.regex_parser import RegexParser
from utils.reader.csv_reader import CsvReader
import numpy as np


class Similarity:
    def __init__(self, model_path, noun_set: set):
        self.model = KeyedVectors.load(model_path)
        self.dim = 300
        self.noun_set = noun_set

    def _get_sum_vector(self, sentence: str):
        sum_vector = np.zeros(self.dim)
        clean_sent = RegexParser.get_clean_sentence(sentence)

        print(f"{clean_sent}")

        count = 0

        for word in clean_sent:
            word_ = self._get_noun_word(word)

            if word_:
                try:
                    sum_vector = np.add(sum_vector, self.model.wv[word_])
                    count += 1
                except KeyError as e:
                    print(e)

        return sum_vector, count

    def _is_in_noun_set(self, word):
        intersec = self.noun_set.intersection({word})
        return True if intersec else False

    def _get_noun_word(self, word) -> None:
        if self._is_in_noun_set(word):
            return word
        elif self._is_in_noun_set(word[:-1]):
            return word[:-1]
        elif self._is_in_noun_set(word[:-2]):
            return word[:-2]

        return None

    def _get_mean_vector(self, sum_vec: np.ndarray, count):
        if count != 0:
            mean_vec = np.divide(sum_vec, count)
        else:
            mean_vec = np.zeros(self.dim)

        return mean_vec

    def get_most_sim(self, sentence: str):
        _sum_vector, _count = self._get_sum_vector(sentence)
        mean_vec = self._get_mean_vector(_sum_vector, _count)

        most_sim = self.model.wv.most_similar(mean_vec, topn=100)

        return most_sim


if __name__ == "__main__":
    model_path = '../word2vec/model/w2v_model'
    nouns_path = '../data/noun_data/nouns.csv'
    nouns = CsvReader.read_single_column(nouns_path)
    sim = Similarity(model_path, set(nouns))

    test_str = "김태리에게 미안해진 보나, 주마등처럼 스쳐가는 막말의 기억"
    res = sim.get_most_sim(test_str)
    print(res)

