from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
from utils.regex.regex_parser import RegexParser
import unittest
import numpy as np


class SimilarityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_str = "아 피자 먹고 싶어!!"

    def test_consine_sim(self):
        model_path = "../word2vec/model/w2v_model"
        model = KeyedVectors.load(model_path, mmap="r")

        vec_1 = model.wv["피자"]
        vec_2 = model.wv["치킨"]
        vec_3 = model.wv["삼겹살"]

        res_1 = cosine_similarity(vec_1.reshape(1, -1), vec_2.reshape(1, -1))
        res_2 = cosine_similarity(vec_1.reshape(1, -1), vec_3.reshape(1, -1))

        self.assertTrue(res_1 > res_2)

    def test_sum_vector(self):
        vec_1 = np.array([1, 2, 3, 4])
        expected = np.array([4., 8., 12., 16.])
        sum_ = np.zeros(4)

        for i in range(4):
            sum_ = np.add(sum_, vec_1)

        self.assertTrue(np.array_equal(sum_, expected))

    def test_mean_vector(self):
        vec_1 = np.array([1, 2, 3, 4])
        expected = np.array([1., 2., 3., 4.])
        sum_ = np.zeros(4)

        for i in range(4):
            sum_ = np.add(sum_, vec_1)

        mean_ = np.divide(sum_, 4)
        self.assertTrue(np.array_equal(mean_, expected))

    def test_most_sim(self):
        model_path = "../word2vec/model/w2v_model"
        model = KeyedVectors.load(model_path, mmap="r")
        sum_vec = np.zeros(300)
        count = 0
        hangul = RegexParser.get_hangul(self.test_str)
        print(hangul)

        for word in hangul:
            try:
                vec = model.wv[word]
                sum_vec = np.add(sum_vec, vec)
                count += 1
            except KeyError as e:
                print(e)

        self.assertTrue(count == 1)

        mean_vec = np.divide(sum_vec, count)
        most_sim = model.wv.most_similar(mean_vec, topn=10)

        self.assertTrue(len(most_sim) == 10)
        self.assertTrue('피자' == most_sim[0][0])


if __name__ == "__main__":
    unittest.main()



