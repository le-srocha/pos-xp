import redis
import json
from flask import current_app
from app.models import redis_connection

r = redis_connection()

class FindByIDClienteModel:
    def FindByID_cliente(cliente_id):
        for key in r.scan_iter():
            if key == cliente_id:
                result = r.hgetall(key)
                return result
            else:
                return 0
