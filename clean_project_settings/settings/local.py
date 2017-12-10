from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['LOCAL_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'brunchblog',
'USER': 'brunchbloguser',
'PASSWORD': 'brunch',
'HOST': 'localhost',
'PORT': '',
	}
}

#INSTALLED_APPS += ['debug_toolbar', ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'clean_project/staticfiles')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'clean_project/static'),
   ]


# Redirect to home URL after login
LOGIN_REDIRECT_URL = '/'