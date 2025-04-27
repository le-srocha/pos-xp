from flask import Blueprint
from app.controllers.cliente_controller import ClienteController

api = Blueprint('api', __name__)
cliente_controller = ClienteController()

@api.route('/clientes', methods=['POST'])
def create_cliente():
    return cliente_controller.create_cliente()

@api.route('/clientes/<cliente_id>', methods=['GET'])
def read_cliente(cliente_id):
    return cliente_controller.read_cliente(cliente_id)

@api.route('/clientes/<cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    return cliente_controller.update_cliente(cliente_id)

@api.route('/clientes/<cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    return cliente_controller.delete_cliente(cliente_id)

@api.route('/clientes/count', methods=['GET'])
def count_clientes():
    return cliente_controller.count_clientes()

@api.route('/clientes', methods=['GET'])
def find_all_clientes():
    return cliente_controller.find_all_clientes()

@api.route('/clientes/name/<name>', methods=['GET'])
def find_cliente_by_name(name):
    return cliente_controller.find_cliente_by_name(name)