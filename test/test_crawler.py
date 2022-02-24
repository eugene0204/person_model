import unittest
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime

class CrawlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.expected_length = 10
        self.topics = []

    def test_naver_movie(self):
        url = "https://movie.naver.com/movie/running/current.naver"
        soup = bs(urllib.request.urlopen(url).read(), "html.parser")
        ul = soup.find("div", class_="keyword_obj first_child").find_all('p', class_="rank_tx")

        self.assertIsNotNone(ul)
        self.assertEqual(len(ul), self.expected_length)

        res = []
        for title in ul:
            text_ = title.get_text().replace(" ", "")
            self.assertEqual(False, text_.isspace())
            res.append(text_)

        self.assertEqual(len(res),self.expected_length )
        self.topics.extend(res)

    def test_nate_crawler(self):
        now = datetime.now().strftime('%Y%m%d%H%M')
        url = 'https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=' + now
        r = requests.get(url).content
        keyword_list = json.loads(r.decode('euc-kr'))
        result = []
        for k in keyword_list:
            text_ = k[1].replace(" ", "")
            self.assertEqual(False, text_.isspace())
            result.append(k[1])

        self.assertIsNotNone(r)
        self.assertEqual(len(result), self.expected_length)

        self.topics.extend(result)

    def test_zum_crawler(self):
        url = 'https://m.search.zum.com/search.zum?method=uni&option=accu&qm=f_typing.top&query='
        html = requests.get(url).content
        soup = bs(html, 'html5lib')
        keyword_list = soup.find('div', {'class': 'list_wrap animate'}).find_all('span', {'class': 'keyword'})
        result = []
        for k in keyword_list:
            text_ = k.text.strip()
            self.assertEqual(False, text_.isspace())
            result.append(k.text.strip())

        self.assertIsNotNone(html)
        self.assertEqual(len(result), self.expected_length)

        self.topics.extend(result)

    def test_google_crawler(self):
        url = 'https://trends.google.com/trends/api/topdailytrends?hl=ko&tz=-540&geo=KR'
        html = requests.get(url).text
        data = json.loads(str(html).split('\n')[1])
        result = []
        for i in range(10):
            text_ = data['default']['trendingSearches'][i]['title'].replace(" ", "")
            print(text_)
            self.assertFalse(text_.isspace())
            result.append(data['default']['trendingSearches'][i]['title'])

        self.assertNotEqual(len(html), 0)
        self.assertEqual(len(result), self.expected_length)

        self.topics.extend(result)
        self.assertEqual(len(self.topics), self.expected_length)



if __name__ == "__main__":
    unittest.main()
