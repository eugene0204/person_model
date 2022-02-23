from pytrends.request import TrendReq

if __name__ == "__main__":
    #pytrends_ = TrendReq(hl="ko", tz=540)
    pytrends_ = TrendReq()

    #res = pytrends_.trending_searches(pn="south_korea")
    res = pytrends_.realtime_trending_searches(pn="KR")
    print(res)