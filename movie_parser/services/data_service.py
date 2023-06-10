import pandas as pd
import json

from movie_parser.api_parser.parser import ApiParser
from movie_parser.data_handler.preprocessor import DataProcessor
from movie_parser.data_handler.converter import DataConverter
from movie_parser.constants import DATA_JSON_PATH, RAW_DATA_CSV_PATH, CONVERTED_DATA_CSV_PATH, \
    CLEAN_DATA_CSV_PATH


class DataService:
    _data: pd.DataFrame
    _parser: ApiParser
    _processor: DataProcessor
    _converter: DataConverter

    def __init__(self):
        self._parser = ApiParser()
        self._converter = DataConverter()
        self._processor = DataProcessor()
        self.process_data()

    def get_data(self):
        return self._data

    def update_data(self, films_amount=30000):
        self.parse_data(films_amount=films_amount)
        self.convert_data()
        self.process_data()

    def _load_csv_data(self, data_path, raw_data=False):
        if raw_data:
            self._data = pd.read_csv(data_path)['docs']
        else:
            self._data = pd.read_csv(data_path)

    def _load_json_data(self, data_path):
        self._data = pd.read_json(data_path)['docs']

    def save_csv_data(self, data_path):
        self._data.to_csv(data_path, index=False)

    def save_json_data(self, data_path):
        with open(data_path, 'w') as f:
            json.dump(self._data.json(), f)

    def parse_data(self, films_amount=30000):
        self._parser.get_data(films_limit=films_amount)
        self._load_json_data(DATA_JSON_PATH)

    def convert_data(self):
        self._data = self._converter.convert_data(self._data)
        self.save_csv_data(CONVERTED_DATA_CSV_PATH)

    def process_data(self):
        self._load_csv_data(CONVERTED_DATA_CSV_PATH)
        self._data = self._processor.process_data(self._data)
        self.save_csv_data(CLEAN_DATA_CSV_PATH)
