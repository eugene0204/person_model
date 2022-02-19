import multiprocessing

from utils.reader.gen_reader import BigSentence
from utils.reader.csv_reader import CsvReader
from utils.writer.csv_writer import CsvWriter
from utils.date.date import Date
from tqdm import tqdm
from multiprocessing import Manager, Process


class SentsParser:
    def __init__(self):
        self.queue = Manager().Queue()
        self.hangul_path = "../../data/hangul_data/"
        self.nouns_path = "../tokenization/data/noun/nouns.csv"
        self.noun_sentence_path = "../../data/training_data/"

        _file_name = Date.get_today() + "_training" + ".csv"
        self.noun_sentence_path += _file_name

    def _get_hangul_sents(self, sentences, nouns):
        noun_sents = []
        words = []
        proc_name = multiprocessing.current_process().name

        for sent in tqdm(sentences, desc=proc_name + "-sents parser"):
            words.clear()
            split = sent.split()
            for word in split:
                if word in nouns and len(word) > 1:
                    words.append(word)

            if len(words) > 1:
                join_ = " ".join(words)
                noun_sents.append(str(join_))

        noun_sents = list(set(noun_sents))

        self.queue.put(noun_sents)

    def _split_sentences(self):
        chunk_size = 10000
        sentences_ = self._get_sentences()

        split_sents = []
        sub_list = []
        count = 0
        for sent in tqdm(sentences_, desc="split sents"):
            if count < chunk_size:
                sub_list.append(sent)
                count += 1
            else:
                count = 0
                split_sents.append(sub_list.copy())
                sub_list.clear()

        if sub_list:
            split_sents.append(sub_list)

        return split_sents


    def _get_noun_sents(self):
        res = []
        while not self.queue.empty():
            sent = self.queue.get()
            res.append(sent)

        hangul_sentences = []
        for sent in res:
            for hangul in sent:
                hangul_sentences.append(hangul)

        return hangul_sentences

    def _get_nouns(self):
        nouns = CsvReader.read_file(self.nouns_path)
        return nouns

    def _get_sentences(self):
        sentences = BigSentence(self.hangul_path)
        return sentences

    def start(self):
        split_sent = self._split_sentences()
        nouns = self._get_nouns()

        processes = []
        for sent in split_sent:
            p = Process(target=self._get_hangul_sents, args=(sent, nouns))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

    def write_file(self):
        noun_sents = self._get_noun_sents()
        CsvWriter.write_csv(path=self.noun_sentence_path,
                            sentences=noun_sents)


if __name__ == "__main__":
    parser = SentsParser()

    parser.start()
    parser.write_file()







