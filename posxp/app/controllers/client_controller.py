from fastapi import HTTPException
from app.models.client_model import ClientModel
from app.schemas.client_schema import Client

client_model = ClientModel()

class ClientController:

    @classmethod
    def create_client(cls, client_data:Client):
        return client_model.create_client(client_data)
    
    @classmethod
    def find_by_id(cls, client_id:str):
        client = client_model.get_client_by_id(client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    
    @classmethod
    def find_all(cls):
        return client_model.get_all_clients()
    
    @classmethod
    def update(cls, client_id: str, client_data: Client):
        if not client_model.get_client_by_id(client_id):
            raise HTTPException(status_code=404, detail="Client not found")
        client_model.update_client(client_id, client_data)
    
    @classmethod
    def delete(cls, client_id:str):
        client_model.delete_client(client_id)

    @classmethod
    def count(cls):
        return client_model.count_clients()
    
    @classmethod
    def find_by_name(cls, name: str):
        return client_model.get_client_by_name(name)
    