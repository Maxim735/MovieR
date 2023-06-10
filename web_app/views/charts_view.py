from web_app.start_engine import engine
from fastapi import APIRouter
from fastapi_class import View

from web_app.constants import NOT_FOUND_ERROR


charts_router = APIRouter()


@View(charts_router)
class CountryTopView:
    @staticmethod
    @charts_router.get('/charts/countries/{country}/{content_type}/{rating_type}/{amount}')
    def get_country_top(country: str, content_type: str = 'movie',
                        rating_type: str = 'imdb', amount: int = 10):
        try:
            top_movie_names = engine.get_country_top(country=country, content_type=content_type,
                                                     rating_type=rating_type)['name'][:amount]
            return {'Top': top_movie_names}
        except KeyError:
            return NOT_FOUND_ERROR.format(element=country)


@View(charts_router)
class GenreTopView:
    @staticmethod
    @charts_router.get('/charts/genres/{genre}/{content_type}/{rating_type}/{amount}')
    def get_genre_top(genre: str, content_type: str = 'movie',
                            rating_type: str = 'imdb', amount: int = 10):
        try:
            top_movie_names = engine.get_genre_top(genre, content_type,
                                                   rating_type)['name'][:amount]
            return {'Top': top_movie_names}
        except KeyError:
            return NOT_FOUND_ERROR.format(element=genre)


@View(charts_router)
class YearTopView:
    @staticmethod
    @charts_router.get('/charts/years/{year}/{content_type}/{rating_type}/{amount}')
    def get_year_top(year: int, content_type: str = 'movie',
                           rating_type: str = 'imdb', amount: int = 10):
        try:
            top_movie_names = engine.get_year_top(year, content_type,
                                                  rating_type)['name'][:amount]
            return {'Top': top_movie_names}
        except KeyError:
            return NOT_FOUND_ERROR.format(element=year)
