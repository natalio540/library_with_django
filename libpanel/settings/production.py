from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['librarywithdjango.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9hi4216lam6bb',
        'USER':'rbmfbvoxewcjmj',
        'PASSWORD':'9220912fb8979b5844d013ae2a24dab5e416d709425329488cae515d6fad0f7a',
        'HOST':'ec2-23-23-88-216.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
    }
}
