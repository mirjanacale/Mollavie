import os
if os.path.exists("env.py"):
    import env
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
load_dotenv()


#  Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

env_path = os.path.join(BASE_DIR, 'env.py')
if os.path.exists(env_path):
    exec(open(env_path).read())


#  Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY') or 'temporary-insecure-key'
DEBUG = os.environ.get('DEBUG') == 'True'
ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1", ".herokuapp.com"]



#  Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'mollavie_shop',
]

#  Cloudinary media config

CLOUDINARY_STORAGE = {
     "CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL") or "cloudinary://dummy:dummy@dummy"
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Stripe config
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")

# 🔧 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

# 🔗 URLs
ROOT_URLCONF = 'mollavie.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'mollavie_shop' / 'templates'],
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

# 🔥 WSGI
WSGI_APPLICATION = 'mollavie.wsgi.application'

# 🛢️ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://localhost',  # fallback for local dev
        conn_max_age=600,
        ssl_require=False  # change to True for production
    )
}

CSRF_TRUSTED_ORIGINS = ["https://*.codeinstitute-ide.net/", "https://*.herokuapp.com"]


# 🔐 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

#  Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

#  Static files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'mollavie_shop' / 'static',
]

# 🆔 Primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = '/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


