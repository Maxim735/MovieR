import numpy as np

DATA_COLS = ['externalId', 'rating', 'votes', 'movieLength', 'id', 'type', 'name',
 'description', 'year', 'poster', 'genres', 'countries', 'alternativeName', 'enName',
 'names', 'shortDescription','logo', 'watchability']

SKIP_DATA_COLS = ['countries', 'names', 'genres', 'watchability']

LIST_FORMAT_DATA_COLS = ['countries', 'names', 'genres']

NAN_COLS = ['externalId tmdb',
       'externalId imdb', 'externalId kpHD', 'watchability START',
       'watchability Иви', 'watchability Okko', 'watchability Wink',
       'watchability KION', 'watchability 24ТВ',
       'watchability НТВ-ПЛЮС Онлайн ТВ', 'watchability viju',
       'watchability Триколор Кино и ТВ', 'watchability PREMIER',
       'watchability Смотрёшка', 'watchability Кино1ТВ',
       'watchability AMEDIATEKA', 'watchability Большое ТВ',
       'watchability more.tv', 'watchability ctc.ru', 'watchability Dомашний',
       'watchability НТВ', 'watchability МегаФон ТВ',
       'poster', 'logo url', 'shortDescription',
       'enName', 'alternativeName', 'poster previewUrl',
       'poster url', 'description', 'name', 'type', 'id']

TO_DROP_COLS = ['externalId tmdb',
       'externalId imdb', 'externalId kpHD', 'watchability START',
       'watchability Иви', 'watchability Okko', 'watchability Wink',
       'watchability KION', 'watchability 24ТВ',
       'watchability НТВ-ПЛЮС Онлайн ТВ', 'watchability viju',
       'watchability Триколор Кино и ТВ', 'watchability PREMIER',
       'watchability Смотрёшка', 'watchability Кино1ТВ',
       'watchability AMEDIATEKA', 'watchability Большое ТВ',
       'watchability more.tv', 'watchability ctc.ru', 'watchability Dомашний',
       'watchability НТВ', 'watchability МегаФон ТВ', 'names', 'genres',
       'logo url', 'enName', 'alternativeName', 'poster previewUrl',
       'poster url', 'id', 'countries', 'poster']

DATA_JSON_PATH = '../CourseWork/movie_parser/data/raw_movies_data.json'

CLEAN_DATA_CSV_PATH = '/home/maksim/Documents/Work/CourseWork/movie_parser/data/clean_movies_data.csv'

RAW_DATA_CSV_PATH = '/home/maksim/Documents/Work/CourseWork/movie_parser/data/raw_movies_data.csv'

CONVERTED_DATA_CSV_PATH = '/home/maksim/Documents/Work/CourseWork/movie_parser/data/converted_movies_data.csv'

MOVIES_PATH = '/home/maksim/Documents/Work/CourseWork/movie_parser/data/movie.csv'

RATINGS_PATH = '/home/maksim/Documents/Work/CourseWork/movie_parser/data/rating.csv'

RU_STOPWORDS_PATH = '/home/maksim/Documents/Work/stopwords-ru.txt'

NAN_STRING_TYPES = ['None', 'NaN', 'null', 'Null', 'nan', np.nan]

EMPTY_INDICES = [4595, 30000]
# empty year column for this indices
NAN_DATA_YEARS_INDICES = [6410, 9971, 10065, 11768, 15351]
EDITED_DATA_YEARS = [1997, 2020, 2019, 2010, 2011]


MOVIE_LENGTH_MEAN = 85
