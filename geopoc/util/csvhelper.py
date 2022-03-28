import pandas as pd


class CsvHelper:
    LAT_COL = 1
    LONG_COL = 2

    def read_next_latlong(self):
        row = self.csv_reader.read(1)
        return row[CsvHelper.LAT_COL], row[CsvHelper.LONG_COL]

    def get_rows_size(self):
        return self.csv_reader.size

    def __init__(self, myfilename):
        self.filename = myfilename
        self.csv_reader = pd.read_csv(self.filename)
