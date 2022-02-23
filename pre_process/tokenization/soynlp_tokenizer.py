from utils.reader.gen_reader import BigSentence
from utils.reader.csv_reader import CsvReader
from utils.writer.csv_writer import CsvWriter
from soynlp.noun import LRNounExtractor_v2
import csv


class SoyNlpTokenizer:
    def __init__(self, hangul_path, noun_path):
        self.hangul_data_path = hangul_path
        self.nouns_data_path = noun_path

    def _train_extract(self):
        sentences = self._get_raw_data()
        noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=True)
        return noun_extractor.train_extract(sentences)

    def _get_nouns_list(self, nouns) -> list:
        noun_list = [noun for noun in nouns if len(noun) > 1]

        return noun_list

    def _get_raw_data(self):
        sentences = BigSentence(self.hangul_data_path)

        return sentences

    def start(self):
        extracted_nouns = self._train_extract()
        new_nouns = self._get_nouns_list(extracted_nouns)

        old_nouns = []
        try:
            old_nouns = CsvReader.read_file(self.nouns_data_path)
        except FileNotFoundError as e:
            print(e)
            pass

        if old_nouns:
            nouns = old_nouns + new_nouns
            nouns = list(set(nouns))
        else:
            nouns = new_nouns


        print(f"old noun size: {len(old_nouns)}")
        CsvWriter.write_csv(self.nouns_data_path, nouns)
        print(f"new noun size: {len(nouns)}")


if __name__ == "__main__":
    tokenizer = SoyNlpTokenizer()
    tokenizer.start()





