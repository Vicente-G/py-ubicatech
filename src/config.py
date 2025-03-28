import os

from dotenv import load_dotenv

load_dotenv()

PORT = int(os.environ.get("PORT", "8000"))
PG_URL = os.environ.get("PG_URL", None)
