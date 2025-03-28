from flask import current_app


def log(*kwargs):
    if current_app.config["DEBUG"]:
        for arg in kwargs:
            current_app.logger.debug(f"{arg=}")
