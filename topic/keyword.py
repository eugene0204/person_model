from array import array


class Keyword:
    topic_set = set()

    def __init__(self, keyword="", rootword=""):
        self.__keyword = keyword
        self.rootwords = []
        if rootword:
            self.rootwords.append(rootword)

    @property
    def keyword(self):
        return self.__keyword

    def __iter__(self):
        yield self

    def __repr__(self):
        return self.keyword

    def __str__(self):
        return self.keyword

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        if self.keyword == other.keyword:
            if len(other.rootwords) == 0:
                other.rootwords = self.rootwords
            return True
        else:
            return False

    def __hash__(self):
        split = self.keyword.split()
        if len(split) > 1:
            for word in split:
                self.topic_set.add(Keyword(word, self.keyword))

        return hash(self.keyword)

    def __bool__(self):
        return bool(self.keyword)




