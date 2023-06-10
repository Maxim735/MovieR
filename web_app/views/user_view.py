from web_app.start_engine import engine
from fastapi import APIRouter, HTTPException
from fastapi_class import View
from web_app.helpers.email_validator import EmailValidator

user_router = APIRouter()


@View(user_router)
class UserView:
    @staticmethod
    @user_router.get('/')
    def hello():
        return {'Hello, ': 'User!'}

    @staticmethod
    @user_router.post('/register/')
    def register_user(username: str = '', email: str = ''):
        if not EmailValidator.check_email(email) \
                or len(username) < 6:
            raise HTTPException(status_code=404, detail="Bad username or email!")

        user_id = len(engine.get_data()) + 1
        return {'UserID': user_id, 'Username': username, 'Email': email}


@View(user_router)
class UserLikeView:
    @staticmethod
    @user_router.get('/review/like/user/')
    def like_movie(user_id: int, movie_id: int, user_rating: float):
        engine.add_user_review(user_id, movie_id, user_rating)
        return 'Updated successfully!'

    @staticmethod
    @user_router.get('/review/delete/user/')
    def delete_review(user_id: int, movie_id: int):
        return engine.delete_user_review(user_id, movie_id)
