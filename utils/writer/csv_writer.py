import csv


class CsvWriter:
    @staticmethod
    def write_csv(path, sentences, mode='w'):
        with open(path, mode, encoding='utf-8') as file:
            writer = csv.writer(file)

            for sent in sentences:
                writer.writerow([sent])

