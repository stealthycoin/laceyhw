
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG=DEBUG
ALLOWED_HOSTS = ['']

ROOT_URLCONF = 'elena.urls'
STATIC_URL = '/static/'
WSGI_APPLICATION = 'elena.wsgi.application'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILE_DIRS = (
    os.path.join(BASE_DIR,'math_history/static/'),
    os.path.join(BASE_DIR,'current_events/static/'),
    os.path.join(BASE_DIR,'science/static/'),
    os.path.join(BASE_DIR,'pe/static/'),
    os.path.join(BASE_DIR,'mathematics/static/'),
    os.path.join(BASE_DIR,'main/static/'),
)

#Middleware classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "main.context_processors.loginForm",
    "main.context_processors.logoutForm",
    "main.context_processors.signupForm",
    "django.core.context_processors.request"
)
SECRET_KEY = '*d+3owzrk0kb5vub=ava!3dffh())5jk6*p2#nxpxm7!c)d(6o'

#Administrators
ADMINS = (
)
MANAGERS = ADMINS

INSTALLED_APPS = (
    'south',
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'math_history',
    'current_events',
    'science',
    'pe',
    'mathematics',
    'main',)

#Template directories
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'math_history/templates'),
    os.path.join(BASE_DIR, 'current_events/templates'),
    os.path.join(BASE_DIR, 'science/templates'),
    os.path.join(BASE_DIR, 'pe/templates'),
    os.path.join(BASE_DIR, 'mathematics/templates'),
    os.path.join(BASE_DIR, 'main/templates')
)
DATABASES = { 'default': {
'ENGINE' : 'django.db.backends.sqlite3', 'NAME' : os.path.join(BASE_DIR, 'elena.db')
} }
