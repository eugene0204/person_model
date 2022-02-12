import csv


class CsvReader:
    @staticmethod
    def read_file(path):
        rows = []
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        return rows
