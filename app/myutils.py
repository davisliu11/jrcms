from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import logging, sys, json_logging, flask

def get_logger(app):
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_flask()
    json_logging.init_request_instrument(app)

    # init the logger as usual
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger

def get_limiter(app):
    return Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["300 per minute", "10 per second"] # default limit
        )