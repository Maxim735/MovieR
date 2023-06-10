from web_app.start_engine import engine
from fastapi import APIRouter
from fastapi_class import View


data_router = APIRouter()


def get_movie_data_by_name(movie_name: str):
    data = engine.get_data()
    try:
        movie = data[data['name'].str.lower() == movie_name.lower()]
        return movie
    except Exception as e:
        return None


def get_movie_ratings(movie_data):
    return {'imdb': movie_data['rating imdb'],
            'await': movie_data['rating await'],
            'filmCritics': movie_data['rating filmCritics'],
            'kp': movie_data['rating kp']}



@View(data_router)
class DataYearView:
    @staticmethod
    @data_router.get('/data/year/{movie_name}')
    def get_movie_year(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        if len(movie_data):
            return {'Year': movie_data['year'].iloc[0]}


@View(data_router)
class DataGenresView:
    @staticmethod
    @data_router.get('/data/genres/{movie_name}')
    def get_movie_genres(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        genres = {'genres': []}
        for col in movie_data.columns:
            if 'is_' in col:
                if movie_data[col].iloc[0] == 1:
                    genres['genres'].append(col[3:])

        return genres


@View(data_router)
class DataCountryView:
    @staticmethod
    @data_router.get('/data/countries/{movie_name}')
    def get_movie_country(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        countries = {'countries': []}
        for col in movie_data.columns:
            if 'from_' in col:
                if movie_data[col].iloc[0] == 1:
                    countries['countries'].append(col[5:])

        return countries


@View(data_router)
class DataDescriptionView:
    @staticmethod
    @data_router.get('/data/description/{movie_name}')
    def get_movie_description(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        return movie_data['description'].iloc[0]


@View(data_router)
class DataRatingView:
    @staticmethod
    @data_router.get('/data/ratings/{movie_name}')
    def get_movie_ratings(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        return get_movie_ratings(movie_data)


@View(data_router)
class DataTypeView:
    @staticmethod
    @data_router.get('data/movie_type/{movie_name}')
    def get_movie_type(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        return movie_data['type']


@View(data_router)
class DataMovieLengthView:
    @staticmethod
    @data_router.get('/data/movie_length/{movie_name}')
    def get_movie_length(movie_name: str):
        movie_data = get_movie_data_by_name(movie_name)
        return movie_data['movieLength'].iloc[0]


@View(data_router)
class DataUpdateView:
    @staticmethod
    @data_router.get('/data/update/{data_amount}')
    def update_data(data_amount):
        engine.update_data(films_amount=data_amount)
        return 'Updated!'
