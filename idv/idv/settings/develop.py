from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = 25

ALLOWED_HOSTS = (
    "localhost",
    "dev.idv.huiser.nl",
)

DATABASES = {
	"default": {
		"ENGINE":	"django.db.backends.postgresql_psycopg2",
		"NAME":		"idv_develop",
		"USER":		"idv_develop",
		"PASSWORD":	"idv",
		"HOST":		"localhost",
		"PORT":		"",
	}
}

INSTALLED_APPS += (
    "debug_toolbar",
)

INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
