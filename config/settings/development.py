from .base import *

MIDDLEWARE.append('config.middleware.dev_cors_middleware')
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append('rest_framework.authentication.SessionAuthentication')
