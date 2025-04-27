from flask import request, jsonify
from app.models.cliente_model import ClienteModel

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()
    
    def create_cliente(self):
        cliente_data = request.get_json()
        cliente_id = cliente_data['id']
        self.model.create_cliente(cliente_id, cliente_data)
        return jsonify({'message': 'Cliente criado com sucesso!'}), 201

    def read_cliente(self, cliente_id):
        cliente = self.model.read_cliente(cliente_id)
        return jsonify(cliente) if cliente else ('Cliente não encontrado', 404)

    def update_cliente(self, cliente_id):
        cliente_data = request.get_json()
        self.model.update_cliente(cliente_id, cliente_data)
        return jsonify({'message': 'Cliente atualizado com sucesso!'})

    def delete_cliente(self, cliente_id):
        self.model.delete_cliente(cliente_id)
        return jsonify({'message': 'Cliente deletado com sucesso!'})

    def count_clientes(self):
        count = self.model.count_clientes()
        return jsonify({'total_clientes': count})

    def find_all_clientes(self):
        clientes = self.model.find_all_clientes()
        return jsonify(clientes)

    def find_cliente_by_name(self, name):
        clientes = self.model.find_cliente_by_name(name)
        return jsonify(clientes)