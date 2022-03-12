from datetime import date
from utils.reader.csv_reader import CsvReader
import tweepy
import csv
import time

access_token = "810489185861824512-sa6J6p1RAaolOFcLh1TOPmuOP9XHmDM"
access_token_secret = "zczOpmqn2vpzIg68XuKhXQgXzE4nMhuJGTu1gGugyV6Mv"
consumer_key = "mYh1sti2PMGKmiU0C8pPLbGGl"
consumer_secret = "0Kf8DNw8HklsHnINLGOPRryZMo3EvSCJvIL0Edh9JKS6ShCfx1"


def write_file(tweet):
    today = date.today()
    current_date = today.strftime("%Y_%m_%d")
    path = "../data/ongoing_data/" + "twitter_" + current_date + ".txt"

    with open(path, 'a') as f:
        f.write(tweet.text)
        f.write('\n')


class MyStreamListener(tweepy.Stream):
    def on_status(self, tweet):
        print(tweet.text)
        write_file(tweet)

    def on_exception(self, exception):
        print(f"Exception:{exception}")

    def on_connection_error(self):
        print("connection error")

    def on_connect(self):
        print("on connect")


def get_filter_words(path):

    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        filter_words = [word[0] for word in csv_reader]

    return filter_words

def split_filter_words(filterwords):
    split_words = []
    chunk_size = 200
    size = len(filterwords)
    for i in range(0, size, chunk_size):
        sub_words = filterwords[i:i + chunk_size]
        split_words.append(sub_words)

    return split_words


if __name__ == "__main__":
    filter_path = "../data/keyword_data/crawler_keyword.csv"
    filter_words = CsvReader.read_single_column(path=filter_path)
    filter_words = list(set(filter_words))
    print(f"filter size: {len(filter_words)}")
    split_words = split_filter_words(filter_words)

    stream = MyStreamListener(consumer_key, consumer_secret, access_token, access_token_secret)
    for words in split_words:
        print("-----------------------------------------------------------------------------")
        stream.filter(track=words, threaded=True)
        time.sleep(600)


