import os

from utils.reader.gen_reader import BigSentence, BigFile
from utils.writer.csv_writer import CsvWriter
from utils.date.date import Date
from tqdm import tqdm
from multiprocessing import Pool, Queue, Process, current_process, Manager
import multiprocessing as mp

import json
import re


class JsonParser:

    def read_file(self, sentences):
        hangul_sentences = []
        for sent in tqdm(sentences, desc="json parser"):
            try:
                json_data = json.loads(sent)
                text = json_data['text']
                hangul = re.findall(u'[\uAC00-\uD7A3]+', text)
                if len(hangul) > 1:
                    hangul_sentences.append(" ".join(hangul))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        return hangul_sentences

    def read_file_with_queue(self, sentences, queue_: Queue):
        hangul_sentences = []
        p_name = current_process().name
        for sent in tqdm(sentences, desc=p_name + "-json parser"):
            try:
                json_data = json.loads(sent)
                text = json_data['text']
                hangul = re.findall(u'[\uAC00-\uD7A3]+', text)
                if len(hangul) > 1:
                    hangul_sentences.append(" ".join(hangul))
            except KeyError as e:
                pass

        hangul_sentences = list(set(hangul_sentences))

        queue_.put(hangul_sentences)

    def get_file_generators(self, path):
        files = os.listdir(path)
        file_gens = []

        for file in files:
            sentences = BigFile(os.path.join(path, file))
            file_gens.append(sentences)

        return file_gens


def start_multiprc(file_gens_, queue: Queue):
    processes = []
    for sent in file_gens_:
        p = Process(target=parser.read_file_with_queue, args=(sent, queue,))
        processes.append(p)

    for p in processes:
        print("process start")
        p.start()


    return processes


if __name__ == "__main__":
    path = "../../data/raw_data/"
    parser = JsonParser()
    queue = Manager().Queue()

    files_gens = parser.get_file_generators(path)
    processes = start_multiprc(files_gens, queue)

    for p in processes:
        print("join")
        p.join()

    res = []
    while not queue.empty():
        sent = queue.get()
        res.append(sent)

    hangul_sentences = []
    for sent in res:
        for hagul in sent:
            hangul_sentences.append(hagul)

    print(len(hangul_sentences))
    hangul_sentences = list(set(hangul_sentences))
    print(len(hangul_sentences))

    file_name = Date.get_today() + "_hagnul" + ".csv"
    hangul_path = "../../data/hangul_data/" + file_name
    CsvWriter.write_csv(hangul_path, hangul_sentences)
