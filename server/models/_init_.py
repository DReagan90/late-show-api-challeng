from server.app import db

# import all models so they register with Flask-Migrate
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance
