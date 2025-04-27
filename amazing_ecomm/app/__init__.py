from flask import Flask
#from app.views.api_view import api
#from app.config import Config
from app.models.CRUD_cliente_model import CRUDClienteModel
from app.models.contagem_cliente_model import CountClienteModel
from app.models.findAll_cliente_model import FindAllClienteModel
from app.models.findByID_cliente_model import FindByIDClienteModel
from app.models.findByName_cliente_model import FindByNameClienteModel

def create_app():
    print('init do app')
    #app = Flask(__name__)
    #app.config.from_object(Config)
    
    #app.register_blueprint(api, url_prefix='/api')

    #return app