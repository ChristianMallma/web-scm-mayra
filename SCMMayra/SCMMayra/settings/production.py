from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['scmmayra.herokuapp.com']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Configurando la base de datos para SCM en PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dddqfbtut4p5fp',
        'USER': 'hnpydouwmfkzbr',
        'PASSWORD': '9aeb6bc400851126f7f2eafd71ca1c3bd19378ffc049a5a218c58ce7f47111c1',
        'HOST': 'ec2-23-21-109-177.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

#Configuración de los archivos multimedia
MEDIA_URL='/media/' #url
MEDIA_ROOT=os.path.join(BASE_DIR,'media')#donde se buscará el contenido de las imágenes

#STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'