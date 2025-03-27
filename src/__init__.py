# Standard Library imports
import os

from dotenv import load_dotenv

# Core Flask imports
# Third-party imports
# App imports
from src.app import create_app, db_manager
from src.app.models import Account, Role, User, UserRole

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == "__main__":
    app = create_app()

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db_manager,
            "User": User,
            "Account": Account,
            "Role": Role,
            "UserRole": UserRole,
        }
