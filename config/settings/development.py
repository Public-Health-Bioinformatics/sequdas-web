from .base import *

MIDDLEWARE += [
    'config.middleware.dev_cors_middleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]
