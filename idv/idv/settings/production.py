from .base import *

DATABASES = {
	"default": {
		"ENGINE":	"django.db.backends.postgresql_psycopg2",
		"NAME":		"idv_prod",
		"USER":		"idv_prod",
		"PASSWORD":	get_env_variable("DB_PASSWORD"),
		"HOST":		"localhost",
		"PORT":		"",
	}
}
