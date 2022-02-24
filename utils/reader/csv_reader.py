import csv


class CsvReader:
    @staticmethod
    def read_file(path, header=False):
        rows = []
        try:
            with open(path, 'r') as f:
                reader = csv.reader(f)

                if header:
                    next(reader)

                for row in reader:
                    rows.append("".join(row))
        except FileNotFoundError as e:
            print(e)

        return rows
