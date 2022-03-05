from pre_process.parser.json_hangul_parser import JsonParser
from pre_process.parser.text_hangul_parser import TextParser
from pre_process.parser.noun_parser import NounParser
from pre_process.tokenization.soynlp_tokenizer import SoyNlpTokenizer

def start():
    raw_data_path = "./data/raw_data/"
    hangul_data_path = "./data/hangul_data/"
    training_data_path = "./data/training_data/"
    noun_data_path = "data/noun_data/nouns.csv"

    sent_parser = TextParser(raw_path=raw_data_path, hangul_path=hangul_data_path)
    tokenizer = SoyNlpTokenizer(hangul_path=hangul_data_path, noun_path=noun_data_path)
    noun_parser = NounParser(hangul_path=hangul_data_path,
                             noun_path=noun_data_path,
                             training_path=training_data_path)

    sent_parser.start_multiprc()
    tokenizer.start()
    noun_parser.start_mutiprc()


if __name__ == '__main__':
    start()

