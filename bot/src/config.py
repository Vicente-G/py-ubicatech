import os

from dotenv import load_dotenv

load_dotenv()

PAGE_SIZE = int(os.environ.get("PAGE_SIZE", 50))
REDIRECT_URL = os.environ.get("REDIRECT_URL", None)
API_URL = os.environ.get("API_URL", None)
