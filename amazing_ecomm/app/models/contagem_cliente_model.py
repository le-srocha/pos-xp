import redis
import json
from flask import current_app
from app.models import redis_connection

r = redis_connection()

class CountClienteModel:
    def count_cliente():
        lastKey = 0
        for key in r.scan_iter():
            lastKey = lastKey + 1
        return lastKey