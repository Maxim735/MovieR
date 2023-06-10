from movie_parser.recommendations.content_recommender import ContentRecommender
from movie_parser.recommendations.user_recommender import UserRecommender


class RecsService:
    _user_recs: UserRecommender
    _content_recs: ContentRecommender

    def __init__(self):
        self._user_recs = UserRecommender()
        self._content_recs = ContentRecommender()

    def update(self):
        self._content_recs.update()
        self._user_recs.update()

    def get_user_recommendation(self, user_id: int):
        return self._user_recs.get_recommendations(user_id)

    def get_year_recommendation(self, title: str):
        return self._content_recs.recommendations_by_year(title)

    def get_genre_recommendation(self, title: str):
        return self._content_recs.recommendations_by_genres(title)

    def get_mixed_recommendation(self, title: str):
        return self._content_recs.get_recommendations(title)
