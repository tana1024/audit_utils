import os
from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ad($!z@i^9$ai@gd!6j4f!7fobv#f8pq%ux44_b=695kd1vf(z' # 追加

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^https://.*.ws-ap.*.gitpod.io$', )


