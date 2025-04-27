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

class FindAllClienteModel:
    def FindAll_cliente():
        return r.scan_iter()