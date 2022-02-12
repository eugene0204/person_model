from utils.reader.gen_reader import BigSentences
from utils.writer.csv_writer import CsvWriter
from soynlp.noun import LRNounExtractor_v2
import csv


class SoyNlpTokenizer:
    def __init__(self):
        pass

    def train_extract(self, sentences):
        noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=True)
        return noun_extractor.train_extract(sentences)

    def read_noun_dict(self, path):
        print(f"reading:{path}")

        with open(path, 'r') as f:
            reader = csv.reader(f)
            nouns = [noun for noun in reader]

        return nouns


if __name__ == "__main__":
   hangul_path = "../../data/hangul_data/"
   nouns_path  = "data/nouns.csv"
   tokenizer = SoyNlpTokenizer()

   sentences = BigSentences(hangul_path)

   nouns = tokenizer.train_extract(sentences)
   CsvWriter.write_csv(nouns_path, nouns)

