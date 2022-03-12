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
                    for item in categorymembers:
                        item_list.append(item)


            except Exception as e:
                print(e)

        print(item_list)
        self._write_file(item_list)


if __name__ == "__main__":
    wiki = WikiCrawler()
    wiki.parse_page("분류:대한민국의_여자_가수")




