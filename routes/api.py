from flask import Blueprint, jsonify, make_response, request
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
api = Blueprint('api', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )

#Lista Personas
#Este es un ejemplo del video del
@api.route('/api/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dic()}),
        200
    )
 
#Guardar personas   
@api.route('/api/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.json
    print(type(data))
    if not "apellido" in data.keys():
        return make_response(
            jsonify({"msg":"Falta Datos", "code": 400, "data": {}}),
            400
        )            
    #Todo..validar
    pd._persona._apellido = data['apellido']
    pd._persona._nombre = data['nombre']
    pd._persona._direccion = data['direccion']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['fono']
    pd._persona._tipoIdentificacion = data['tipo']
    pd.save
    return make_response(
        jsonify({"msg":"OK se ha registrado correctamente", "code": 200, "data":{}}),
        200
    )    