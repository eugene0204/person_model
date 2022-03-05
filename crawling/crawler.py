import urllib.request
import requests
import time
import schedule
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime
from utils.writer.csv_writer import CsvWriter
from utils.reader.csv_reader import CsvReader


class Crawler:
    def __init__(self):
        self.topics = []
        self.filter_path = "../data/filter_data/crawler_filter.csv"

    def naver_movie_crawler(self):
        url = "https://movie.naver.com/movie/running/current.naver"
        soup = bs(urllib.request.urlopen(url).read(), "html.parser")
        ul = soup.find("div", class_="keyword_obj first_child").find_all('p', class_="rank_tx")

        res = []
        for title in ul:
            res.append(title.get_text().replace(" ", ""))

        print(res)

        self.topics.extend(res)

        return res



    def nate_crawler(self):
        now = datetime.now().strftime('%Y%m%d%H%M')
        url = 'https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=' + now
        r = requests.get(url).content
        keyword_list = json.loads(r.decode('euc-kr'))

        res = []
        for k in keyword_list:
            res.append(k[1].replace(" ", ""))

        print(res)
        self.topics.extend(res)
        return res



    def zum_crawler(self):
        url = 'https://m.search.zum.com/search.zum?method=uni&option=accu&qm=f_typing.top&query='
        html = requests.get(url).content
        soup = bs(html, 'html5lib')
        keyword_list = soup.find('div', {'class' : 'list_wrap animate'}).find_all('span', {'class' : 'keyword'})
        result = []
        for k in keyword_list:
            result.append(k.text.strip().replace(" ", ""))

        print(result)
        self.topics.extend(result)
        return result


    def google_crawler(self):
        url = 'https://trends.google.com/trends/api/topdailytrends?hl=ko&tz=-540&geo=KR'
        html = requests.get(url).text
        data = json.loads(str(html).split('\n')[1])
        result = []
        for i in range(10):
            result.append(data['default']['trendingSearches'][i]['title'].replace(" ", ""))
        print(result)
        self.topics.extend(result)
        return result

    def get_all_topics(self):
        print(self.topics)
        print(len(self.topics))

        return self.topics

    def write_file(self):
        topics = []
        new_topics = list(set(self.topics))
        old_topics = CsvReader.read_file(self.filter_path)

        if old_topics:
            topics = new_topics + old_topics
            topics = list(set(topics))
        else:
            topics = new_topics

        CsvWriter.write_csv(self.filter_path, topics)
        print(len(topics))

def start():
    crawler = Crawler()

    crawler.naver_movie_crawler()
    crawler.nate_crawler()
    crawler.zum_crawler()
    crawler.google_crawler()
    crawler.get_all_topics()

    crawler.write_file()

schedule.every(10).minutes.do(start)

if __name__ == "__main__" :
    while True:
        schedule.run_pending()
        time.sleep(1)
