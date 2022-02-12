from utils.reader.gen_reader import BigSentences
from utils.writer.csv_writer import CsvWriter
import json
import re


class JsonParser:
    def __init__(self, path):
        self.sentences = BigSentences(path)

    def read_file(self):
        hangul_sentences = []
        for sent in self.sentences:
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


if __name__ == "__main__":
    path = "../data/raw_data/"
    parser = JsonParser(path)
    sentences = parser.read_file()

    hangul_path = "../data/hangul_data/21_5_3.csv"
    CsvWriter.write_csv(hangul_path, sentences)
