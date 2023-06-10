import pandas as pd

from ..constants import  NAN_STRING_TYPES, TO_DROP_COLS, \
    NAN_DATA_YEARS_INDICES, \
    MOVIE_LENGTH_MEAN, EDITED_DATA_YEARS, \
    EMPTY_INDICES


class DataProcessor:
    _df: pd.DataFrame
    _NEED_RESET_INDICES = False

    def process_data(self, df):
        self._df = df
        self._filter_data()
        self._create_genres_features()
        self._create_countries_features()
        self._change_columns_types()
        self._clear_data()
        return self._df

    def _change_columns_types(self):
        self._df['movieLength'] = pd.to_numeric(self._df['movieLength'])
        self._df['year'] = pd.to_numeric(self._df['year'])

    def _clear_data(self):
        for col in TO_DROP_COLS:
            if col in self._df:
                self._df = self._df.drop(columns=[col])

        for index in EMPTY_INDICES:
            if len(self._df) > index:
                self._df = self._df.drop([index])

        self._df = self._df.drop([len(self._df) - 1])

        no_name_indices = self._df[self._df['name'] == ''].index.values.tolist()
        for index in no_name_indices:
            if len(self._df) > index:
                self._df = self._df.drop([index])
        self._check_on_reset_indices()

    def _filter_data(self):
        self._fill_nans()

    def _create_genres_list(self):
        self._df = self._df.reset_index()
        genres_list = []
        for i in range(len(self._df['genres']) - 1):
            split_list = self._df['genres'].iloc[i].split('^')
            for el in split_list:
                genres_list.append(el)

        genres_list = set(genres_list)
        genres_list.remove('')
        return genres_list

    def _create_genres_features(self):
        genres_list = self._create_genres_list()
        for genre in genres_list:
            self._df.loc[:, 'is_' + genre] = 0

        for genre in genres_list:
            self._df.loc[(self._df['genres'].str.find(genre) != -1), 'is_' + genre] += 1

    def _create_countries_list(self):
        countries_list = []
        for i in range(len(self._df['countries']) - 1):
            split_list = self._df['countries'].iloc[i].split('^')
            for el in split_list:
                countries_list.append(el)

        countries_list = set(countries_list)
        countries_list.remove('')
        return countries_list

    def _create_countries_features(self):
        countries_list = self._create_countries_list()

        for country in countries_list:
            self._df.loc[:, 'from_' + country] = 0
        for country in countries_list:
            self._df.loc[(self._df['countries'].str.find(country) != -1), 'from_' + country] += 1

    def _fill_nans(self):
        self._df.loc[(self._df['movieLength'].isnull()), 'movieLength'] = MOVIE_LENGTH_MEAN

        for i, index in enumerate(NAN_DATA_YEARS_INDICES):
            if index < len(self._df['year']):
                self._df['year'].iloc[index] = EDITED_DATA_YEARS[i]

        for col in self._df.columns:
            self._df[col] = self._df[col].replace(NAN_STRING_TYPES, '')

    def _check_on_reset_indices(self):
        if self._NEED_RESET_INDICES:
            self._df = self._df.reset_index()
            self._NEED_RESET_INDICES = False


