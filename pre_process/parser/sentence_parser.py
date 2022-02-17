from utils.reader.gen_reader import BigSentences
from utils.reader.csv_reader import CsvReader
from utils.writer.csv_writer import CsvWriter
from utils.date.date import Date
from tqdm import tqdm


class SentsParser:
    def get_hangul_sents(self, sentences, nouns):
        noun_sents = []
        words = []
        for sent in tqdm(sentences, desc="sents parser"):
            words.clear()
            split = sent.split()
            for word in split:
                if word in nouns and len(word) > 1:
                    words.append(word)

            if len(words) > 1:
                join_ = " ".join(words)
                noun_sents.append(str(join_))

        noun_sents = list(set(noun_sents))

        return noun_sents



if __name__ == "__main__":
    hangul_path = "../../data/hangul_data/"
    nouns_path = "../tokenization/data/noun/nouns.csv"
    noun_sentence_path = "../../data/training_data/"

    file_name = Date.get_today() + ".csv"
    noun_sentence_path += file_name

    nouns = CsvReader.read_file(nouns_path)
    sentences = BigSentences(hangul_path)
    parser = SentsParser()

    noun_sents = parser.get_hangul_sents(sentences, nouns)

    CsvWriter.write_csv(path=noun_sentence_path, sentences=noun_sents)






