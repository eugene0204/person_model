from utils.writer.csv_writer import CsvWriter
import wikipediaapi

class WikiCrawler:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('ko')
        self.path = "../data/temp/wiki.csv"

    def _write_file(self, sentences: list):
        CsvWriter.write_csv(self.path, sentences, mode='a')


    def parse_page(self, keyword: str):
        page = self.wiki.page(keyword)
        item_list = []
        if page.exists():
            try:
                sections = page.sections
                categorymembers = page.categorymembers

                if sections:
                    for sub in sections:
                        names = sub.text
                        split = names.split("\n")
                        item_list.extend(split)

                elif categorymembers:
                    for item in categorymembers.items():
                        for sub_item in item[1].categorymembers:
                            item_list.append(sub_item)

            except Exception as e:
                print(e)
        item_list = list(set(item_list))
        print(item_list)
        self._write_file(item_list)



if __name__ == "__main__":
    page_list = ("분류:팀별_KBO_리그_선수")
    wiki = WikiCrawler()
    wiki.parse_page()




