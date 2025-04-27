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

class CRUDClienteModel:
    def create_cliente(cliente_id, cliente_name, cliente_surname):
        success = r.hset(cliente_id, 'Nome', cliente_name)
        success = r.hset(cliente_id, 'Sobrenome', cliente_surname)

                
        #lastKey = 0
        #for key in r.scan_iter():
        #    lastKey = lastKey + 1