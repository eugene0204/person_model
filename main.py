from pre_process.parser.json_sent_parser import JsonParser
from pre_process.parser.text_sent_parser import TextParser
from pre_process.parser.noun_parser import NounOnlySentParser
from pre_process.tokenization.soynlp_tokenizer import SoyNlpTokenizer

def start():
    raw_data_path = "./data/raw_data/"
    clean_sent_data_path = "./data/clean_sent_data/"
    training_data_path = "./data/training_data/"
    noun_data_path = "data/noun_data/nouns.csv"

    json_sent_parser = JsonParser(raw_path=raw_data_path, clean_path=clean_sent_data_path)
    #text_sent_parser = TextParser(raw_path=raw_data_path, clean_path=clean_sent_data_path)
    tokenizer = SoyNlpTokenizer(clean_path=clean_sent_data_path, noun_path=noun_data_path)
    noun_sent_parser = NounOnlySentParser(clean_path=clean_sent_data_path,
                                          noun_path=noun_data_path,
                                          training_path=training_data_path)

    #text_sent_parser.start_multiprc()
    json_sent_parser.start_multiprc()
    tokenizer.start()
    noun_sent_parser.start_mutiprc()


if __name__ == '__main__':
    start()

