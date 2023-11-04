"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os
# import pymysql
# pymysql.install_as_MySQLdb()



AWS_API_URL = os.getenv("AWS_API_URL")
print(AWS_API_URL)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b-dx4ca++p=xg@d3$#0cmts5a0km&ute9%j7c&v%zi_8i(he&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    AWS_API_URL,
    '127.0.0.1'
    ]
# START SCRIPT
# script to resolve AWS EB health check issue as described here
# https://hashedin.com/blog/5-gotchas-with-elastic-beanstalk-and-django/


# def is_ec2_linux():
#     """Detect if we are running on an EC2 Linux Instance
#        See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
#     """
#     if os.path.isfile("/sys/hypervisor/uuid"):
#         with open("/sys/hypervisor/uuid") as f:
#             uuid = f.read()
#             return uuid.startswith("ec2")
#     return False


# def get_linux_ec2_private_ip():
#     """Get the private IP Address of the machine if running on an EC2 linux server"""
#     from urllib.request import urlopen
#     if not is_ec2_linux():
#         return None
#     try:
#         response = urlopen(
#             'http://169.254.169.254/latest/meta-data/local-ipv4')
#         return response.read()
#     except:
#         return None
#     finally:
#         if response:
#             response.close()


# ElasticBeanstalk healthcheck sends requests with host header = internal ip
# So we detect if we are in elastic beanstalk,
# and add the instances private ip address
# private_ip = get_linux_ec2_private_ip()
# if private_ip:
#     ALLOWED_HOSTS.append(private_ip)

# END SCRIPT

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.apps.ApiConfig',
    'corsheaders',
    'markdownx',
    # 'ebhealthcheck.apps.EBHealthCheckConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
print('ASDFGHJKLLKJHGFDSA: ', os.getenv("SQL_DB_HOST"))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     'NAME': os.getenv("SQL_DB_NAME"),
    #     'USER': os.getenv("SQL_DB_USERNAME"),
    #     'PASSWORD': os.getenv("SQL_DB_PASSWORD"),
    #     'HOST': os.getenv("SQL_DB_HOST"),
    #     'PORT': os.getenv("SQL_DB_PORT"),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'staticfiles/'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [

    "http://localhost:5173",

]

print('API Key: ', AWS_API_URL)
