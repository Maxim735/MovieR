from fastapi import APIRouter
from fastapi_class import View

from web_app.start_engine import engine
from web_app.constants import NOT_FOUND_ERROR


recs_router = APIRouter()


@View(recs_router)
class UserRecommenderView:
    @staticmethod
    @recs_router.get('/recommendations/user/{user_id}')
    def get_user_recs(user_id: int):
        try:
            recs_titles = engine.get_user_recommendations(user_id)['title']
            return {'Movies': [recs_titles]}
        except Exception:
            return NOT_FOUND_ERROR.format(element=user_id)


@View(recs_router)
class ContentRecommenderView:
    @staticmethod
    @recs_router.get('/recommendations/content/genres/{movie_title}')
    def get_genre_based_recs(movie_title: str):
        try:
            recs_titles = engine.get_recommendations_by_genre(movie_title)['title']
            return {'Movies': [recs_titles]}
        except Exception:
            return NOT_FOUND_ERROR.format(element=movie_title)

    @staticmethod
    @recs_router.get('/recommendations/content/years/{movie_title}')
    def get_year_based_recs(movie_title: str):
        try:
            recs_titles = engine.get_recommendations_by_year(movie_title)['title']
            return {'Movies': [recs_titles]}
        except Exception:
            return NOT_FOUND_ERROR.format(element=movie_title)

    @staticmethod
    @recs_router.get('/recommendations/content/{movie_title}')
    def get_content_recs(movie_title: str):
        try:
            recs_titles = engine.get_content_recommendations(movie_title)['title']
            return {'Movies': [recs_titles]}
        except Exception:
            return NOT_FOUND_ERROR.format(element=movie_title)
