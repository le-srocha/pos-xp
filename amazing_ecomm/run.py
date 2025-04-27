from app import create_app
from app.models.CRUD_cliente_model import CRUDClienteModel

app = create_app()

cliente = CRUDClienteModel.update_cliente(2,'Nome 21','Sobrenome 2')
#delete = CRUDClienteModel.delete_cliente(2)
#lastKey = 0
#for key in findall:
#    lastKey = lastKey + 1
#    print(lastKey)

#print(findall)

#if __name__ == '__main__':
#    app.run(debug=True)