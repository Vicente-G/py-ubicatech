import logging

from colorama import Fore, Style
from flask import has_request_context, request


def custom_filter(record):
    if "production WSGI" in record.msg:
        return False
    return " - - " not in record.msg


class ColorFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.DEBUG:
            record.levelname = f"{Fore.LIGHTWHITE_EX}[{record.levelname}]"
        elif record.levelno == logging.INFO:
            record.levelname = f"{Fore.LIGHTBLACK_EX}[{record.levelname}]"
        elif record.levelno == logging.WARNING:
            record.levelname = f"{Fore.LIGHTYELLOW_EX}[{record.levelname}]"
        elif record.levelno == logging.ERROR:
            record.levelname = f"{Fore.LIGHTRED_EX}[{record.levelname}]"
        elif record.levelno == logging.CRITICAL:
            record.levelname = f"{Fore.RED}[{record.levelname}]"
        record.msg = f"{record.msg}{Style.RESET_ALL}"
        if has_request_context():
            record.name = f"{request.remote_addr} -> {request.path}"
        else:
            record.name = "server"
        record.name = f"({Fore.LIGHTMAGENTA_EX}{record.name}{Style.RESET_ALL})"
        return super().format(record)


def setup_logging():
    logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    formatter = ColorFormatter(
        "|%(asctime)s| %(name)s> %(levelname)s - %(message)s",
        f"{Fore.LIGHTBLUE_EX}%Y-%m-%d %H:%M:%S{Style.RESET_ALL}",
    )
    console_handler.setFormatter(formatter)
    console_handler.addFilter(custom_filter)
    logger.addHandler(console_handler)

    return logger
