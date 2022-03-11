from array import array


class Keyword:
    typecode = 'd'

    def __init__(self, keyword=""):
        self.__keyword = keyword

    @property
    def keyword(self):
        return self.__keyword

    def __iter__(self):
        print("iter")
        split = self.keyword.split()
        split.append(self.keyword)
        return (Keyword(word) for word in split)


    def __repr__(self):
        print("repr")
        return type(self).__name__ + self.keyword

    def __str__(self):
        print("str")
        return self.keyword

    def __eq__(self, other):
        print("eq")
        split = set(other.keyword.split())
        my_split = set(self.keyword.split())
        intersection = split.intersection(my_split)

        return True if intersection else False

    def __hash__(self):
        print("hash")
        return hash(self.keyword)


    def __bool__(self):
        return bool(self.keyword)



    def get_sub_string(self):
        return self.sub_str




