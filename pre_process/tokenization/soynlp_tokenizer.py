from utils.reader.gen_reader import BigSentence
from utils.reader.csv_reader import CsvReader
from utils.writer.csv_writer import CsvWriter
from soynlp.noun import LRNounExtractor_v2
import csv



class SoyNlpTokenizer:
    def __init__(self):
        pass

    def train_extract(self, sentences):
        noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=True)
        return noun_extractor.train_extract(sentences)

    def get_nouns_list(self, nouns) -> list:
        noun_list = []
        for noun_ in nouns:
            if len(noun_) > 1:
                noun_list.append(noun_)

        return noun_list


if __name__ == "__main__":
    training_path = "data/training_data/"
    nouns_path = "data/noun/nouns.csv"
    tokenizer = SoyNlpTokenizer()

    sentences = BigSentence(training_path)

    extracted_nouns = tokenizer.train_extract(sentences)
    new_nouns = tokenizer.get_nouns_list(extracted_nouns)

    old_nouns = []
    try:
        old_nouns = CsvReader.read_file(nouns_path)
    except FileNotFoundError as e:
        print(e)

    if old_nouns:
        nouns = old_nouns + new_nouns
        nouns = list(set(nouns))
    else:
        nouns = new_nouns

    CsvWriter.write_csv(nouns_path, nouns)



