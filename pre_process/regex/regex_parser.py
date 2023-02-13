import re


class RegexParser:

    @staticmethod
    def get_hangul(sentence: str):
        hangul = re.findall(u'[\uAC00-\uD7A3]+', sentence)
        return hangul

    @staticmethod
    def get_clean_sentence(sentence: str) -> str:
        sent = sentence
        RT = "RT"

        split = sent.split()
        try:
            if RT == split[0]:
                split = split[1:]
                sent = " ".join(split)

            url_pattern = r"(http\S+)"
            sent = re.sub(url_pattern, "", sent)

            id_pattern = r"@\S+"
            sent = re.sub(id_pattern, "", sent)

            pattern = '[\uAC00-\uD7AF\d\u0041-\u005A\u0061-\u007A\u0025]+'
            sent = re.findall(pattern, sent)
        except IndexError as e:
            pass

        return sent

if __name__ == "__main__":
    test_str = "RT @mola_mola44: 이재명 41% -윤석열 46.1%…尹, 호남서 30%대 지지율 ˙선전˙ [리얼미터](출처: MBN | 네이버 뉴스) https://t.co/gDe5tyHszp"
    sent = RegexParser.get_clean_sentence(test_str)
    print(sent)

