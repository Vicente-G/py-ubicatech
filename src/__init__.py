import argparse
import logging

from flask import Flask, current_app, redirect, request, url_for

from src.config import PORT
from src.database import init_db
from src.logs import setup_logging
from src.routes import docs_bp
from src.routes.cpu import cpu_bp

setup_logging()


def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(docs_bp)
    app.register_blueprint(cpu_bp)

    @app.errorhandler(404)
    def handle_404(e):
        current_app.logger.warning(
            f"HTTP/{request.method}: Route not found, redirecting to home"
        )
        return redirect(url_for("docs.home")), 302

    if __name__ != "__main__":
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.setLevel(gunicorn_logger.level)
    app.logger.info("App started")
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Flask app.")
    parser.add_argument(
        "--debug", action="store_true", help="Run the app in debug mode."
    )
    parser.add_argument("--host", type=str, help="Host to run the app on.")
    args = parser.parse_args()

    app = create_app()
    app.run(host=args.host, port=PORT, debug=args.debug)
