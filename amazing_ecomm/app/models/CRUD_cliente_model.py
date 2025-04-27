import redis
import json
from flask import current_app
from app.config import REDIS
from app.models import redis_connection

class CRUDClienteModel:
#    def redis_connection():
#        conn = json.loads(REDIS)

#        r = redis.Redis(
#                host=conn["URL"],
#                port=conn["port"],
#                decode_responses=True,
#                username=conn["username"],
#                password=conn["password"],
#            )
#        return r
        
    def create_cliente(cliente_id, cliente_name, cliente_surname):
        r = redis_connection()
        success = r.hset(cliente_id, 'Nome', cliente_name)
        success = r.hset(cliente_id, 'Sobrenome', cliente_surname)

    def update_cliente(cliente_id, cliente_name, cliente_surname):
        cliente = CRUDClienteModel.create_cliente(cliente_id,cliente_name,cliente_surname)

    def delete_cliente(cliente_id):
        r = redis_connection()
        delete = r.delete(cliente_id)