import os

from django_demo.settings import BASE_DIR

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]

LOGIN_REDIRECT_URL = '/'