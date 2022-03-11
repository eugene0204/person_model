import unittest
import wikipediaapi


class TestWiki(unittest.TestCase):
    def setUp(self) -> None:
        self.wiki = wikipediaapi.Wikipedia('ko')

    def test_parse(self):
        page = self.wiki.page("두산_베어스_역대_선수_목록")
        name_list = []
        if page.exists():
            try:
                sections = page.sections
                for sub in sections:
                    names = sub.text
                    split = names.split("\n")
                    name_list.extend(split)
            except Exception as e:
                print(e)

            if '정수빈' in name_list:
                self.assertTrue(True)






if __name__ == "__main__":
    unittest.main()

