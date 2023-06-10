import re

EMAIL_VALIDATION_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class EmailValidator:
    @staticmethod
    def check_email(email):
        return re.fullmatch(EMAIL_VALIDATION_REGEX, email)
