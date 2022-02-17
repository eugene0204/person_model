import csv


class CsvWriter:
    @staticmethod
    def write_csv(path, sentences):
        with open(path, 'w') as file:
            writer = csv.writer(file)

            for sent in sentences:
                writer.writerow([sent])
