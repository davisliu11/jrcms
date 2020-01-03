from flask_redis import FlaskRedis
import os

class ContentManager():
    def __init__(self, app):
        redis_host = os.environ.get("REDIS_HOST", default="127.0.0.1")
        redis_port = os.environ.get("REDIS_PORT", default="6379")
        app.config['REDIS_URL'] = f"redis://{redis_host}:{redis_port}"
        self.app = app
        self.redis_client = None

    def _get_redis_client(self):
        if self.redis_client:
            return self.redis_client
        self.redis_client = FlaskRedis(self.app)
        return self.redis_client

    def get_content(self, contentKey):
        return self._get_redis_client().get(contentKey)

    def set_content(self, contentKey, contentValue):
        return self._get_redis_client().set(contentKey, contentValue)
