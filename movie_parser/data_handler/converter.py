import pandas as pd

from movie_parser.constants import DATA_COLS, SKIP_DATA_COLS, \
    LIST_FORMAT_DATA_COLS


class DataConverter:
    _df = None

    def convert_data(self, df):
        self._df = df
        my_df = pd.DataFrame()
        for i in range(30000):
            temp_df = pd.DataFrame(index=[0])
            try:
                if self._df[i]['watchability']['items']:
                    for elem in self._df[i]['watchability']['items']:
                        temp_df.insert(0, 'watchability ' + elem['name'], elem['url'])
            except (KeyError, TypeError) as e:
                continue

            for col in DATA_COLS:
                try:
                    if col in SKIP_DATA_COLS:
                        continue
                    elif isinstance(self._df[i][col], dict):
                        for sub_col in self._df[i][col].keys():
                            temp_df.insert(0, col + ' ' + sub_col, self._df[i][col][sub_col])
                    else:
                        temp_df.insert(0, col, str(self._df[i][col]))
                except (KeyError, TypeError) as e:
                    continue

            for col in LIST_FORMAT_DATA_COLS:
                try:
                    added = ''
                    for el in self._df[i][col]:
                        added += ''.join(el.values()) + '^'
                    temp_df.insert(0, col, added)
                except (KeyError, TypeError) as e:
                    continue
            my_df = pd.concat([temp_df, my_df])

        return my_df
