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
    def __init__(self, raw_path, clean_path):
        self.raw_data_path = raw_path
        self.clean_data_path = clean_path
        self.queue = Manager().Queue()

    def read_file(self, sentences):
        hangul_sentences = []
        for sent in tqdm(sentences, desc="json parser"):
            try:
                json_data = json.loads(sent)
                text = json_data['text']
                clean_sent = RegexParser.get_clean_sentence(text)

                if len(clean_sent) > 1:
                    hangul_sentences.append(" ".join(clean_sent))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        return hangul_sentences

    def _read_file_with_queue(self, sentences):
        clean_sentences = []
        p_name = current_process().name
        for sent in tqdm(sentences, desc=p_name + "-json parser"):
            try:
                json_data = json.loads(sent)
                text = json_data['text']
                clean_sent = RegexParser.get_clean_sentence(text)

                if len(clean_sent) > 1:
                    clean_sentences.append(" ".join(clean_sent))
            except KeyError as e:
                pass

        clean_sentences = list(set(clean_sentences))

        self.queue.put(clean_sentences)

    def _get_file_generators(self, path):
        files = os.listdir(path)
        file_gens = []

        for file in files:
            sentences = BigFile(os.path.join(path, file))
            file_gens.append(sentences)

        return file_gens

    def _get_clean_sentence(self):
        res = []
        while not self.queue.empty():
            sent = self.queue.get()
            res.append(sent)

        clean_sentences = []
        for sent in res:
            for hagul in sent:
                clean_sentences.append(hagul)

        print(len(clean_sentences))
        clean_sentences = list(set(clean_sentences))
        print(len(clean_sentences))

        return clean_sentences

    def _write_file(self, clean_sentences):
        file_name = Date.get_today() + "_clean" + ".csv"
        clean_path = self.clean_data_path + file_name
        CsvWriter.write_csv(clean_path, clean_sentences)

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

        clean_sents = self._get_clean_sentence()
        self._write_file(clean_sents)


if __name__ == "__main__":
    parser = JsonParser()
    parser.start_multiprc()


