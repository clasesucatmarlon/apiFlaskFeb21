from flask import Flask
from flask import request
from flask import jsonify
from flask import json

app = Flask(__name__)

users = [ 
            {'id': 1, 'nombre': 'Marlon', 'apellido': 'Garcia', 'edad': '48'},
            {'id': 2, 'nombre': 'Marol', 'apellido': 'Garcia', 'edad': '46'},
            {'id': 3, 'nombre': 'Leidy', 'apellido': 'Gandica', 'edad': '38'}
]

# CONSULTAR TODOS LOS USUSRIOS
# ***************************************************************************
@app.route('/users', methods=['GET'])
def getAllUsers():
    return jsonify(users), 200


# CONSULTAR USUARIOS POR id
# ***************************************************************************
@app.route('/users/<id>', methods=['GET'])
def getAllUsersbyId(id):
    result = next((user for user in users if user['id'] == int(id)), None)
    if result is not None:
        return jsonify(result), 200
    else:
        return 'Usuario no encontrado', 404


# CREAR USUARIO
# ***************************************************************************
@app.route('/users', methods=['POST'])
def addUsers():
    body = json.loads(request.data) # Convierte en objeto de python
    # Captura de elementos
    idUser = body['id']
    nombreUser = body['nombre']
    apellidoUser = body['apellido']
    edadUser = body['edad']
    # Crear objeto con el nuevo usuario
    newUser = {
        'id': idUser,
        'nombre': nombreUser,
        'apellido': apellidoUser,
        'edad': edadUser
    }
    # Agregar usuario al json
    users.append (newUser)
    # Convertir objeto de python en json y retornarlo
    return jsonify(newUser), 200


# ELIMINAR USUARIO
# ***************************************************************************
@app.route('/users/<id>', methods=['DELETE'])
def deleteUsers(id):
    userFound = None
    for index, user in enumerate(users):
        if user['id'] == int(id):
            userFound = user
            users.pop(index)
    if userFound is not None:
        return "Eliminado exitosamente", 200
    else:
        return "No existe el registro", 404


# ACTUALIZAR USUARIO
# ***************************************************************************
@app.route('/users/<id>', methods=['PUT'])
def updateUsers(id):
    body = json.loads(request.data) # Convierte en objeto de python
    # Captura de elementos
    newIdUser = body['id']
    newNombreUser = body['nombre']
    newApellidoUser = body['apellido']
    newEdadUser = body['edad']
    # Crear objeto con el los datos modificados
    updateUser = {
        'id': newIdUser,
        'nombre': newNombreUser,
        'apellido': newApellidoUser,
        'edad': newEdadUser
    }

    userUp = None
    for index, user in enumerate(users):
        if user['id'] == int(id):
            userUp = updateUser
            users[index] = updateUser

    if userUp is not None:
        return "Actualizado exitosamente", 200
    else:
        return "No existe el registro", 404




if __name__ == '__main__':
    app.run(debug=True)