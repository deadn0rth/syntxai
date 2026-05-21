import os


BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "5"))
RETRY_COUNT = int(os.getenv("RETRY_COUNT", "1"))
