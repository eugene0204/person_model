import os


class BigSentences:
    def __init__(self, path, split=False):
        self.split = split
        self.path = path

    def __iter__(self):
        files = os.listdir(self.path)
        for file in files:
            with open(os.path.join(self.path, file)) as f:
                for line in f:
                    if self.split:
                        yield line.split()
                    else:
                        yield line


if __name__ == "__main__":
    hangul_path = "../../data/training_data/"

    sentences = BigSentences(hangul_path)
    for sent in sentences:
        pass
