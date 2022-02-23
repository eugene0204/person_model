from multiprocessing import Process, Queue, current_process, Manager
from tqdm import tqdm
from utils.reader.gen_reader import BigFile
from utils.reader.gen_reader import BigSentence
from utils.writer.csv_writer import CsvWriter
from utils.date.date import Date
import os
import re

class TextParser:
    def __init__(self, raw_path, hangul_path):
        self.raw_data_path = raw_path
        self.hangul_data_path = hangul_path
        self.queue = Manager().Queue()


    def _read_file(self, sentences):
        hangul_sentences = []
        for sent in tqdm(sentences, desc="text parser"):
            try:
                hangul = re.findall(u'[\uAC00-\uD7A3]+', sent)
                if len(hangul) > 1:
                    hangul_sentences.append(" ".join(hangul))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        return hangul_sentences


    def _read_file_with_queue(self, sentences):
        hangul_sentences = []
        p_name = current_process().name
        for sent in tqdm(sentences, desc=p_name + "-json parser"):
            try:
                hangul = re.findall(u'[\uAC00-\uD7A3]+', sent)
                if len(hangul) > 1:
                    hangul_sentences.append(" ".join(hangul))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        self.queue.put(hangul_sentences)

    def _get_file_generators(self, path):
        files = os.listdir(path)
        file_gens = []

        for file in files:
            sentences = BigFile(os.path.join(path, file))
            file_gens.append(sentences)

        return file_gens

    def _get_hangul_sentence(self):
        res = []
        while not self.queue.empty():
            sent = self.queue.get()
            res.append(sent)

        hangul_sentences = []
        for sent in res:
            for hagul in sent:
                hangul_sentences.append(hagul)

        print(len(hangul_sentences))
        hangul_sentences = list(set(hangul_sentences))
        print(len(hangul_sentences))

        return hangul_sentences

    def _write_file(self, hangul_sentences):
        file_name = Date.get_today() + "_hagnul" + ".csv"
        hangul_path = self.hangul_data_path + file_name
        CsvWriter.write_csv(hangul_path, hangul_sentences)

    def start_multiprc(self):
        file_gens = self._get_file_generators(self.raw_data_path)

        processes = []
        for sent in file_gens:
            p = Process(target=self._read_file_with_queue, args=(sent, ))
            processes.append(p)

        for p in processes:
            print("process start")
            p.start()

        for p in processes:
            print("join")
            p.join()

        hangul_sentences = self._get_hangul_sentence()
        self._write_file(hangul_sentences)

    def start(self):
        sentences = BigSentence(self.raw_data_path)
        hangul_sentences = self._read_file(sentences)

        file_name = Date.get_today() + "_hagnul" + ".csv"
        hangul_data_path = self.hangul_data_path + file_name
        CsvWriter.write_csv(hangul_data_path, hangul_sentences)


if __name__ == "__main__":
    parser = TextParser()
    parser.start()
