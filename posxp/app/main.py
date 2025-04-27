from fastapi import FastAPI
from app.views.client_view import router as client_router

app = FastAPI()

#incluindo as rotas do cliente
app.include_router(client_router, prefix="/clients", tags=["clients"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Clientes!"}