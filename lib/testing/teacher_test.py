from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def _init_(self, first_name, last_name):
        super()._init_(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        return random.choice(self.knowledge)