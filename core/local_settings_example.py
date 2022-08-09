ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database configuration
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "example_db",
#         "USER": "postgres",
#         "PASSWORD": "admin",
#         "HOST": "localhost",
#         "PORT": "5432",
#         "ATOMIC_REQUESTS": True,
#     }
# }

HOST = "http://localhost:8000"

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
#         "KEY_PREFIX": "lenta",
#     },
# }

# # CELERY
# BROKER_URL = "amqp://localhost"
# CELERY_RESULT_BACKEND = "rpc://"
# CELERY_ACCEPT_CONTENT = ["application/json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_AMQP_TASK_RESULT_EXPIRES = 1000
# CELERY_TIMEZONE = "Asia/Tashkent"
