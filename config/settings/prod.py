from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = [
    "",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
    }
}
