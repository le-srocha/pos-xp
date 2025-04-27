from fastapi import APIRouter
from app.controllers.client_controller import ClientController
from app.schemas.client_schema import Client

router = APIRouter()

@router.post("/")
async def create_client(client: Client):
    return ClientController.create_client(client)

@router.get("/{client_id}")
async def read_client(client_id:str):
    return ClientController.find_by_id(client_id)

@router.get("/")
async def read_all_clients():
    return ClientController.find_all()

@router.put("/{client_id}")
async def update_client(client_id:str, client: Client):
    ClientController.update(client_id, client)

@router.delete("/{client_id}")
async def delete_client(client_id:str):
    ClientController.delete(client_id)

@router.get("/count")
async def count_clients():
    return {"total_clients":ClientController.count()}

@router.get("/by_name/{name}")
async def get_client_by_name(name:str):
    return ClientController.find_by_name(name)