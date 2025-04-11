import os

from dotenv import load_dotenv

load_dotenv()


DEFAULT_TARGET_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../../migrations/atlas/data"
)

PAGE_SIZE = int(os.environ.get("PAGE_SIZE", 50))
TARGET_FOLDER = os.environ.get("TARGET_FOLDER", DEFAULT_TARGET_FOLDER)

REDIRECT_URL = os.environ.get("REDIRECT_URL", None)
API_URL = os.environ.get("API_URL", None)
