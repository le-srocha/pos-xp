import redis
import json
from flask import current_app
from app.config import REDIS

conn = json.loads(REDIS)

r = redis.Redis(
        host=conn["URL"],
        port=conn["port"],
        decode_responses=True,
        username=conn["username"],
        password=conn["password"],
    )

class CountClienteModel:
    def count_cliente():
        lastKey = 0
        for key in r.scan_iter():
            lastKey = lastKey + 1
        return lastKey