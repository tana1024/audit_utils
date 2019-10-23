import os
from socket import gethostname

SECRET_KEY = 'ad($!z@i^9$ai@gd!6j4f!7fobv#f8pq%ux44_b=695kd1vf(z' # 追加

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^https://.*.ws-ap0.gitpod.io$', )

DEBUG = True
