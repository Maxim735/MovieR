import pandas as pd

from movie_parser.services.data_service import DataService
from movie_parser.top_creator.create_genres_top import TopCreator
from movie_parser.constants import CLEAN_DATA_CSV_PATH
from movie_parser.ratings_updater.ratings_update import RatingsUpdater
from movie_parser.services.recs_service import RecsService

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class RecsEngine:
    _data: pd.DataFrame
    _data_service: DataService
    _top_creator: TopCreator
    _recommender: RecsService
    _ratings_updater: RatingsUpdater

    def __init__(self):
        self._data_service = DataService()
        self._top_creator = TopCreator()
        self.process_data()

        self._recommender = RecsService()
        self._ratings_updater = RatingsUpdater()

    def get_data(self):
        return self._data_service.get_data()

    def update_data(self, films_amount=30000):
        self.parse_data(films_amount=films_amount)
        self.convert_data()
        self.process_data()

    def parse_data(self, films_amount=30000):
        self._data_service.parse_data(films_amount)
        self._data = self._data_service.get_data()

    def convert_data(self):
        self._data = self._data_service.convert_data()
        self._data = self._data_service.get_data()

    def process_data(self):
        self._data_service.process_data()
        self._data_service.get_data()

    def get_genre_top(self, genre, content_type, rating_type='imdb'):
        self._data = self.get_data()
        return self._top_creator.get_genre_top(self._data, genre=genre, rating_type=rating_type,
                                               content_type=content_type)

    def get_unloved_mix_top(self, lovely_genre, unloved_genre, content_type, rating_type='imdb'):
        self._data = self.get_data()
        return self._top_creator.get_genre_no_mix_top(self._data, lovely_genre=lovely_genre, unloved_genre=unloved_genre,
                                                      rating_type=rating_type, content_type=content_type)

    def get_country_top(self, country, content_type, rating_type='imdb'):
        self._data = self.get_data()
        return self._top_creator.get_country_top(self._data, country=country, rating_type=rating_type,
                                                 content_type=content_type)

    def get_year_top(self, year, content_type, rating_type='imdb'):
        self._data = self._data_service.get_data()
        return self._top_creator.get_year_top(self._data, year=year, rating_type=rating_type, content_type=content_type)

    def get_recommendations_by_genre(self, movie_title):
        return self._recommender.get_genre_recommendation(movie_title)

    def get_recommendations_by_year(self, movie_title):
        return self._recommender.get_year_recommendation(movie_title)

    def get_content_recommendations(self, movie_title):
        return self._recommender.get_mixed_recommendation(movie_title)

    def get_user_recommendations(self, user_id):
        return self._recommender.get_user_recommendation(user_id)

    def add_user_review(self, user_id, movie_id, rating):
        self._ratings_updater.add_review(user_id, movie_id, rating)
        self._recommender.update()

    def delete_user_review(self, user_id, movie_id):
        result = self._ratings_updater.delete_review(user_id, movie_id)
        if result:
            return result
        else:
            return 'Review didn\'t find!'
