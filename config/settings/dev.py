from .base import *

SECRET_KEY = "9s=85-zgc)nn!ues2ubh4me2!s(v=uqzm@lp8*0l*aav+1r$10"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "celero_db",
        "USER": "celero",
        "PASSWORD": "celero",
    }
}
