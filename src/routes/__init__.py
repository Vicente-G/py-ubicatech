from flask import Blueprint, current_app, request

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/docs")
def home():
    current_app.logger.info(f"HTTP/GET: {request.remote_addr} Redirected successfully")
    return (
        r"""
        <html>
            <h1>404</h1>
            <h3>Route not found, try on \[ /cpus \]</h3>
            <h3>This should be replaced with a docs view soon!</h3>
        </html>""",
        404,
    )
