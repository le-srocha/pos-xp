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

class FindByNameClienteModel:
    def FindByName_cliente(cliente_name):
        for key in r.scan_iter():
            result = r.hgetall(key)
            if result["Nome"] == cliente_name:
                return result
                break
            else:
                return 0
