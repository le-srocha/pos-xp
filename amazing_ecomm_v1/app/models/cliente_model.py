import redis
import json
from flask import current_app

class ClienteModel:
    def __init__(self):
        self.redis = redis.from_url(current_app.config['REDIS_URL'])

    def create_cliente(self, cliente_id, cliente_data):
        self.redis.set(cliente_id, json.dumps(cliente_data))
    
    def read_cliente(self, cliente_id):
        cliente_data = self.redis.get(cliente_id)
        return json.loads(cliente_data) if cliente_data else None

    def update_cliente(self, cliente_id, cliente_data):
        self.redis.set(cliente_id, json.dumps(cliente_data))
    
    def delete_cliente(self, cliente_id):
        self.redis.delete(cliente_id)
    
    def count_clientes(self):
        return len(self.redis.keys())
    
    def find_all_clientes(self):
        clientes = [json.loads(self.redis.get(key)) for key in self.redis.keys()]
        return clientes
    
    def find_cliente_by_name(self, name):
        clientes = [json.loads(self.redis.get(key)) for key in self.redis.keys()]
        return [cliente for cliente in clientes if cliente.get('nome') == name]