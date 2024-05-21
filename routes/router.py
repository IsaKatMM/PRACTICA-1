from flask import Blueprint, jsonify, abort, request, render_template, redirect, Flask
""" from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
from flask import send_file """
from controls.CommandHistoryController import CommandHistoryController
from flask import render_template

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Asociar el Blueprint 'router' a la aplicación Flask
router = Blueprint('router', __name__)

#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
@router.route('/')
def home():
    return render_template("template.html")

# Crear una instancia del controlador
controller = CommandHistoryController()
#funcion add comand que va a guardar los comandos en la variable comand con el metodo add comandd to stack
@router.route('/add_command', methods=['POST'])
def add_command():
    command = request.form['command']
    controller.add_command_to_stack(command)
    #para que me retorme a la misma pagina
    return redirect('/')


#funcion view C, que en la variable comandas guarda con el metodo del controlador LOAD f J
@router.route('/view_commands')
def view_commands():
    commands = controller.load_from_json()
    #con ese metodo me retorna la renderizacion del template, me lo almacena en otra variable denominada comands
    return render_template('template.html', commands=commands)      


# Registrar el Blueprint 'router' en la aplicación Flask
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug=True)


""" 
#Lista Personas
#Este es un ejemplo del video del
@router.route('/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return render_template("nene/lista.html", lista=pd.to_dic())

@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")

@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos)-1)
    return render_template("nene/editar.html", data=nene)


#Guardar personas   
@router.route('/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form

    if not "apellido" in data.keys():
        abort(400)            
    #Todo..validar
    pd._persona._apellido = data['apellido']
    pd._persona._nombre = data['nombre']
    pd._persona._direccion = data['dir']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['fono']
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)


@router.route('/personas/modificar', methods=['POST'], )
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = pd._list().get(int(pos)-1)
    if not "apellido" in data.keys():
        abort(400)            
    #Todo..validar
    pd._persona = nene
    pd._persona._nombre = data['nombre']
    pd._persona._apellido = data['apellido']
    pd._persona._direccion = data['dir']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['fono']
    #pd._persona._tipoIdentificacion = data['tipo']
    pd.merge(int (pos)-1)
    return redirect("/personas", code=302) """