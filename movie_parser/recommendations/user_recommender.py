from sklearn.neighbors import NearestNeighbors
import pandas as pd

from movie_parser.constants import MOVIES_PATH, RATINGS_PATH
from .metrics_calculators import ComputeMetrics
from .helpers import DataFinder, RecsBuilder


class UserRecommender:
    _movies: pd.DataFrame
    _ratings: pd.DataFrame
    _movies_features: pd.DataFrame
    _genres_data: pd.DataFrame
    _mixed_model: NearestNeighbors

    def __init__(self):
        self.update()

    def update(self):
        self._movies = pd.read_csv(MOVIES_PATH)
        self._ratings = pd.read_csv(RATINGS_PATH)
        print(len(self._ratings))
        self._prepare_data()
        self._fit_mixed_model()

    def _prepare_data(self):
        self._genres_data = self._movies['genres'].str.get_dummies('|')
        self._movies_features = self._movies.drop(columns=['title', 'genres'], inplace=False)
        self._movies_features = pd.merge(self._movies_features, self._genres_data, left_index=True, right_index=True)

    def _fit_mixed_model(self):
        self._mixed_model = NearestNeighbors(n_neighbors=3, metric=ComputeMetrics.compute_distance)
        self._mixed_model.fit(pd.DataFrame(self._movies_features.iloc[:, 1:]))

    def get_recommendations(self, user_id):
        ratings_per_user = DataFinder.get_ratings_per_user(self._ratings, user_id)
        recommendations = pd.DataFrame()
        for index, row in ratings_per_user.iterrows():
            movie_id = int(row['movieId'])
            rating = row['rating']
            features = pd.DataFrame(self._movies_features.iloc[DataFinder
                                    .find_index_by_id(self._movies, movie_id), 1:]).transpose()
            recs_by_movie = RecsBuilder.recommend_movies(self._movies, movie_id, features, self._mixed_model)
            recs_by_movie['relevance'] = (1 + recs_by_movie['distance'] * (1/rating))
            recommendations = pd.concat([recommendations, recs_by_movie], ignore_index=True)

        return recommendations
