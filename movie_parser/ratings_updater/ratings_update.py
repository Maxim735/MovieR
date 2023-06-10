import pandas as pd

from movie_parser.constants import RATINGS_PATH


class RatingsUpdater:
    _ratings: pd.DataFrame

    def __init__(self):
        self._ratings = pd.read_csv(RATINGS_PATH)

    def add_review(self, user_id, movie_id, rating):
        review_element = self._ratings[(self._ratings['userId'] == user_id) & (self._ratings['movieId'] == movie_id)]
        if len(review_element):
            index = review_element.index[0]
            self._ratings.loc[index] = [user_id, movie_id, rating]
        else:
            temp_df = pd.DataFrame([[user_id, movie_id, rating]], columns=['userId', 'movieId', 'rating'], index=None)
            self._ratings = pd.concat([self._ratings, temp_df]).reset_index()
            self._ratings.to_csv(RATINGS_PATH)

    def delete_review(self, user_id, movie_id):
        review_element = self._ratings[(self._ratings['userId'] == user_id) & (self._ratings['movieId'] == movie_id)]
        if len(review_element):
            index = review_element.index[0]
            self._ratings = self._ratings.drop(index).reset_index()
            self._ratings.to_csv(RATINGS_PATH)
            return 'Deleted successfully!'
