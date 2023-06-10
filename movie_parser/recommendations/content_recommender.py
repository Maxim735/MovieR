import pandas as pd
from sklearn.neighbors import NearestNeighbors

from movie_parser.constants import MOVIES_PATH
from .metrics_calculators import ComputeMetrics
from .helpers import RecsBuilder, DataFinder


class ContentRecommender:
    movies: pd.DataFrame
    genres_data: pd.DataFrame
    movies_features: pd.DataFrame
    genres_model: NearestNeighbors
    year_model: NearestNeighbors
    mixed_model: NearestNeighbors

    def __init__(self):
        self.update()

    def update(self):
        self.movies = pd.read_csv(MOVIES_PATH)
        self._prepare_data()
        self._fit_genre_model()
        self._fit_year_model()
        self._fit_mixed_model()

    def _prepare_data(self):
        self.genres_data = self.movies['genres'].str.get_dummies('|')
        self.movies_features = self.movies.drop(columns=['title', 'genres'], inplace=False)
        self.movies_features = pd.merge(self.movies_features, self.genres_data, left_index=True, right_index=True)

    def _fit_genre_model(self):
        self.genres_model = NearestNeighbors(n_neighbors=10, metric='cosine')
        self.genres_model.fit(self.movies_features.iloc[:, 2:])

    def _fit_year_model(self):
        self.year_model = NearestNeighbors(n_neighbors=10, metric='euclidean')
        self.year_model.fit(pd.DataFrame(self.movies_features.iloc[:, 1]))

    def _fit_mixed_model(self):
        self.mixed_model = NearestNeighbors(n_neighbors=10, metric=ComputeMetrics.compute_distance)
        self.mixed_model.fit(pd.DataFrame(self.movies_features.iloc[:, 1:]))

    def get_recommendations(self, title):
        index = DataFinder.find_idx_by_title(self.movies, title)
        return RecsBuilder.recommend_movies(self.movies, index,
                                            pd.DataFrame(self.movies_features.iloc[index, 1:]).transpose(),
                                            self.mixed_model)

    def recommendations_by_genres(self, title):
        index = DataFinder.find_idx_by_title(self.movies, title)
        return RecsBuilder.recommend_movies(self.movies, index,
                                            pd.DataFrame(self.movies_features.iloc[index, 2:]).transpose(),
                                            self.genres_model)

    def recommendations_by_year(self, title):
        index = DataFinder.find_idx_by_title(self.movies, title)
        return RecsBuilder.recommend_movies(self.movies, index,
                                            pd.DataFrame(self.movies_features.iloc[index, 1:2]).transpose(),
                                            self.year_model)
