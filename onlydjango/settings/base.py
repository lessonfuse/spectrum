import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)
PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_DIR.parent
WSGI_APPLICATION = "onlydjango.wsgi.application"

FIRST_PARTY_APPS = [
]

ALL_AUTH_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.telegram",
    # # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.telegram',
    # 'allauth.socialaccount.providers.apple',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.microsoft',
]

THIRD_PARTY_APPS = [
    "django_browser_reload",
    "huey.contrib.djhuey",
    'django_cotton',
    "debug_toolbar",
    "crispy_forms",
    "crispy_tailwind",
    "django_flatpickr",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
]

INSTALLED_APPS = (DJANGO_APPS + ALL_AUTH_APPS + THIRD_PARTY_APPS +
                  FIRST_PARTY_APPS)

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

SITE_ID = 1
CSRF_TRUSTED_ORIGINS = ["https://onlydjango.com", "https://www.onlydjango.com"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.auth.middleware.LoginRequiredMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # all-auth
    "allauth.account.middleware.AccountMiddleware",
    # br
    "django_browser_reload.middleware.BrowserReloadMiddleware",

]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Default Django authentication
    "allauth.account.auth_backends.AuthenticationBackend",  # Django Allauth
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = "onlydjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "OPTIONS": {
            "loaders": [(
                "django.template.loaders.cached.Loader",
                [
                    "django_cotton.cotton_loader.Loader",
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ],
            )],
            "builtins": [
                "django_cotton.templatetags.cotton"
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Indian/Maldives"
USE_I18N = False
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# All-auth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_STORE_TOKENS = True
SOCIALACCOUNT_ONLY = True

SOCIALACCOUNT_PROVIDERS = {
    'telegram': {
        'APP': {
            'client_id': os.getenv("TELEGRAM_BOT_ID"),
            'secret': os.getenv("TELEGRAM_BOT_TOKEN"),
        },
        'AUTH_PARAMS': {'auth_date_validity': 30},
    }
}

SITE_VERSION = "0.0.1"
SITE_NAME = os.getenv("SITE_NAME")
