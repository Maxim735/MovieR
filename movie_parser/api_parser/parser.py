import requests
import json
import pandas as pd

from movie_parser.constants import RAW_DATA_CSV_PATH, DATA_JSON_PATH
from movie_parser.tokens import WEB_API_TOKEN


class ApiParser:
    _token = ''
    _base_url = ''

    def __init__(self, token=WEB_API_TOKEN, base_url='https://api.kinopoisk.dev'):
        self.__token = token
        self.__base_url = base_url

    def get_data(self, films_limit=30000):
        response = requests.get(f'{self.__base_url}/v1/movie?limit={films_limit}',
                                headers={'X-API-KEY': self.__token})
        self._save_data(response)

    @staticmethod
    def _save_data(response):
        with open(DATA_JSON_PATH, 'w') as f:
            json.dump(response.json(), f)
        df = pd.read_json(DATA_JSON_PATH)
        df.to_csv(RAW_DATA_CSV_PATH)
