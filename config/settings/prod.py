from .base import *
from decouple import config
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "https://testcelero.herokuapp.com",
]

DATABASES = {"default": dj_database_url.parse(config("DATABASE_URL"))}
