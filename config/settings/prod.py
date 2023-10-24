from .base import *
import environ

ALLOWED_HOSTS = ['zth.kr']
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
CSRF_TRUSTED_ORIGINS = ['https://zth.kr']