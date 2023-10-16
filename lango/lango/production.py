"""
lango production settings file
python manage.py runserver --settings=lango.production
"""

from .base import *
import environ

env = environ.Env(DEBUG=bool, ALLOWED_HOSTS=list)
env_file = BASE_DIR / '..' /'.env'
environ.Env.read_env(env_file=env_file, overwrite=True)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

print("You are using production settings file\n")