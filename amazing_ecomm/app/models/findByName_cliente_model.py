import redis
import json
from flask import current_app
from app.models import redis_connection

r = redis_connection()

class FindByNameClienteModel:
    def FindByName_cliente(cliente_name):
        for key in r.scan_iter():
            result = r.hgetall(key)
            if result["Nome"] == cliente_name:
                return result
            else:
                return 0
