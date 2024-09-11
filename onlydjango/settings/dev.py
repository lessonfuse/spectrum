from os import path
from .base import * # noqa
from huey import RedisHuey
import os
DEBUG = True
ALLOWED_HOSTS = [
    "*",
]
SECRET_KEY = "1234"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Use any S3 Compatible storage backend for static and media files
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_CUSTOM_DOMAIN = "cdn.onlydjango.com"
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {
            "location": path.join(BASE_DIR, "staticfiles"), # noqa
            "base_url": "/static/",
        },
    },
    "media": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
}

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") # noqa
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"), # noqa
]
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# POSTGRES
# noinspection DuplicatedCode
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
        "OPTIONS": {
            "pool": {
                "min_size": 2,
                "max_size": 4,
                "timeout": 10,
            }
        },
    }
}

# Cache settings
# https://docs.djangoproject.com/en/5.0/topics/cache/#setting-up-the-cache
REDIS_URL = os.environ["REDIS_URL"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Tasks backend
HUEY = RedisHuey(url=REDIS_URL)

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "INFO",
        "handlers": ["console"],
        "propagate": "True",
    },
    "loggers": {
        "telegram_logger": {
            "handlers": ["telegram"],
            "level": "ERROR",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "telegram": {
            "level": "DEBUG",
            "class": "onlydjango.telegram_logging.TelegramBotHandler",
            "telegram_bot_token": TELEGRAM_BOT_TOKEN,
            "telegram_chat_id": TELEGRAM_CHAT_ID,
        },
    },

}
