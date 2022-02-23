class NaverDataLabApi:
    def __init__(self, id, secret):
        self.client_id = "l8zWDOivMv_EHVpGepCl"
        self.clined_secret = "mu4H8Ro1QH"
        self.url = "https://openapi.naver.com/v1/datalab/search"

import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.naver"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

ul = soup.find("div", class_ = "keyword_obj first_child").find_all('p',class_="rank_tx")
print(type(ul))
for i, title in enumerate(ul):
    print(title.get_text())

