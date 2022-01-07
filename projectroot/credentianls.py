from decouple import (
    config,
)

secret_key = config('SECRET_KEY', default='')
debug      = config('DEBUG', cast=bool, default=True)

allowed_hosts = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

db_name = config('DB_NAME', default='db.sqlite3')
db_port = config('DB_PORT', cast=int, default='5432')
db_user = config('DB_USER', default='postgres')
db_password = config('DB_PASSWORD', default='')
db_engine   = config('DB_ENGINE', default='django.db.backends.sqlite3')

email_backend       = config("EMAIL_BACKEND", default='django.core.mail.backends.smtp.EmailBackend')
email_use_tls       = config("EMAIL_USE_TLS", cast=bool, default=True)
email_host          = config("EMAIL_HOST", default='smtp.gmail.com')
email_host_user     = config("EMAIL_HOST_USER", default='dovurovjamshid95@gmail.com')
email_host_password = config("EMAIL_HOST_PASSWORD")
email_port          = config("EMAIL_PORT", cast=int, default=587)