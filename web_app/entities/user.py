import datetime


class User:
    id: int
    email: str
    username: str
    registration_time: datetime

    def __init__(self):
        self.id = None
        self.username = 'Unknown'
        self.email = 'Unknown'
        self.registration_time = datetime.datetime.now()

    def set_name(self, new_name):
        self.username = new_name

    def set_email(self, email):
        self.email = email
