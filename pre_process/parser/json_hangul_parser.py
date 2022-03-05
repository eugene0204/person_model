from utils.reader.gen_reader import BigCorpora, BigFile
from utils.writer.csv_writer import CsvWriter
from utils.date.date import Date
from utils.regex.regex_parser import RegexParser
from tqdm import tqdm
from multiprocessing import Pool, Queue, Process, current_process, Manager
import os
import json

#For json format file
class JsonParser:
    def __init__(self, raw_path, hangul_path):
        self.raw_data_path = raw_path
        self.hanul_data_path = hangul_path
        self.queue = Manager().Queue()

    def read_file(self, sentences):
        hangul_sentences = []
        for sent in tqdm(sentences, desc="json parser"):
            try:
                json_data = json.loads(sent)
                text = json_data['text']
                hangul = RegexParser.get_hangul(text)
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
                json_data = json.loads(sent)
                text = json_data['text']
                hangul = RegexParser.get_hangul(text)
                if len(hangul) > 1:
                    hangul_sentences.append(" ".join(hangul))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        self.queue_.put(hangul_sentences)

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
        hangul_path = self.hanul_data_path + file_name
        CsvWriter.write_csv(hangul_path, hangul_sentences)

    def start_multiprc(self):

        file_gens_ = self._get_file_generators(self.raw_data_path)

        processes = []
        for sent in file_gens_:
            p = Process(target=self._read_file_with_queue, args=(sent, ))
            processes.append(p)

        for p in processes:
            print("process start")
            p.start()

        for p in processes:
            print("join")
            p.join()

        hangul_sents = self._get_hangul_sentence()
        self._write_file(hangul_sents)


if __name__ == "__main__":
    parser = JsonParser()
    parser.start_multiprc()


