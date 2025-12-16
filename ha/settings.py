from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------
# 🔐 مفتاح التشفير
# -----------------------------
SECRET_KEY = 'django-insecure-((nwr1%i8hd#v=$+t_vh#b6m=^62bb%@3*&ojrlx_pjke8b5i!'
DEBUG = True
ALLOWED_HOSTS = []


# -----------------------------
# 🔵 التطبيقات
# -----------------------------
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🔵 التطبيقات الخاصة بك
    'accounts.apps.AccountsConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
]


# -----------------------------
# 🔵 وسطيات Django
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------
# 🔵 ضبط الـ URLs
# -----------------------------
ROOT_URLCONF = 'ha.urls'


# -----------------------------
# 🔵 نظام القوالب Templates
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 📌 تعريف مجلد templates الرئيسي
        'DIRS': [BASE_DIR / "templates"],

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


# -----------------------------
# 🔵 WSGI
# -----------------------------
WSGI_APPLICATION = 'ha.wsgi.application'


# -----------------------------
# 🔵 قاعدة البيانات
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------
# 🔵 التحقق من كلمات المرور
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------
# 🔵 اللغة والمنطقة الزمنية
# -----------------------------
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# -----------------------------
# 🔵 الملفات الثابتة Static Files
# -----------------------------
STATIC_URL = '/static/'

# مجلد static داخل المشروع
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# مجلد التجميع collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"


# -----------------------------
# 🔵 ملفات الميديا Media Files
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
