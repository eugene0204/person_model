from utils.reader.gen_reader import BigSentences
from utils.reader.csv_reader import CsvReader
from utils.writer.csv_writer import CsvWriter


class SentsParser:
    def get_hangul_sents(self, sentences, nouns):
        noun_sents = []
        words = []
        for sent in sentences:
            words.clear()
            for word in sent.split():
                if [word] in nouns:
                    words.append(word)

            if len(words) > 1:
                noun_sents.append(words.copy())

        return noun_sents



if __name__ == "__main__":
    hangul_path = "../../data/hangul_data/"
    noun_path = "../tokenization/data/nouns.csv"

    nouns = CsvReader.read_file(noun_path)
    sentences = BigSentences(hangul_path)
    parser = SentsParser()

    noun_sents = parser.get_hangul_sents(sentences, nouns)






