import csv
import pandas as pd

class CsvReader:
    @staticmethod
    def read_single_column(path, header=False):
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

    @staticmethod
    def read_mutil_columns(path):
        col_list = []
        try:
            df = pd.read_csv(path)
            for col in df:
                col_list.extend(df[col].to_list())

        except FileNotFoundError as e:
            print(e)

        return list(set(col_list))




