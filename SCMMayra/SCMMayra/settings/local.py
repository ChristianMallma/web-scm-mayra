from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Configurando la base de datos para SCM en PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mayrascm',
        'USER': 'mayrascm',
        'PASSWORD': 'mayrascm',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#Configuración de los archivos multimedia
MEDIA_URL='/media/' #url
MEDIA_ROOT=os.path.join(BASE_DIR,'media')#donde se buscará el contenido de las imágenes


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'