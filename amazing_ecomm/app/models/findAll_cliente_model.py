import redis
import json
from flask import current_app
from app.models import redis_connection

r = redis_connection()

class FindAllClienteModel:
    def FindAll_cliente():
        return r.scan_iter()