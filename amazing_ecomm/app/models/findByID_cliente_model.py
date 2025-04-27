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

class FindByIDClienteModel:
    def FindByID_cliente(cliente_id):
        for key in r.scan_iter():
            if key == cliente_id:
                result = r.hgetall(key)
                return result
                break
            else:
                return 0
