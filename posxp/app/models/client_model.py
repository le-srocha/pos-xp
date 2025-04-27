from app.services.redis_connection import redis_client
from app.schemas.client_schema import Client

class ClientModel:

    def create_client(self, client_data: Client):
        client_id = str(client_data.id)
        redis_client.hset(client_id, mapping=client_data.dict())
        return client_id
    
    def get_client_by_id(self, client_id:str):
        return redis_client.hgetall(client_id)
    
    def get_all_clients(self):
        return [redis_client.hgetall(key) for key in redis_client.keys()]
    
    def update_client(self, client_id:str, client_data: Client):
        redis_client.hset(client_id, mapping=client_data.dict())
    
    def delete_client(self, client_id:str):
        redis_client.delete(client_id)

    def count_clients(self):
        return len(redis_client.keys())
    
    def get_client_by_name(self, name:str):
        clients = [redis_client.hgetall(key) for key in redis_client.keys()]
        return [client for client in clients if client.get("name")==name]
