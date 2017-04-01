from cargo_exchange.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
	'localhost',
	'.herokuapp.com',
]

SECRET_KEY = get_env_variabel("SECRET_KEY")