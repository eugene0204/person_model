import os


class BigSentences:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        files = os.listdir(self.path)
        for file in files:
            with open(os.path.join(self.path, file)) as f:
                for line in f:
                    yield line


class W2vTrainingSentences:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        files = os.listdir(self.path)
        for file in files:
            with open(os.path.join(self.path, file)) as f:
                for line in f:
                    yield line.split()
