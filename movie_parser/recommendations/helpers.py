import pandas as pd


class DataFinder:
    @staticmethod
    def find_index_by_id(movies, movie_id):
        idx = movies[movies['movieId'] == movie_id].index
        return idx[0]

    @staticmethod
    def get_ratings_per_user(ratings, user_id):
        user_ratings = ratings[ratings['userId'] == user_id]
        user_ratings = user_ratings.drop(['userId'], axis=1)
        return user_ratings

    @staticmethod
    def find_idx_by_title(movies, title):
        try:
            idx = movies[title == movies['title']].index
            return idx[0]
        except IndexError:
            idx = movies[movies['title'].str.find(title) != -1].index
            return idx[0]

    @staticmethod
    def find_title_by_idx(movies, idx):
        title = movies['title'][idx]
        return title


class RecsBuilder:
    @staticmethod
    def recommend_movies(movies, movie_idx, features, model):
        distances, indices = model.kneighbors(features)

        recommended = pd.DataFrame([movies.loc[idx] for idx in indices.flatten()])
        recommended['distance'] = distances.flatten()

        return recommended
