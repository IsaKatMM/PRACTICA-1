#importar el json para guardar los datos y es sistem operation para la ubicacion del archivo
import json
import os
#importando el modelo creado
from models.CommandHistoryModel import CommandHistoryModel 

#inicializando la carpeta donde se guarda DATA
data_folder = 'data'
#clase
class CommandHistoryController:
    def __init__(self):
        #se inicializa como arreglo ´vacio
        self.commands = []

    def add_command_to_stack(self, command):  # Cambia el nombre del método aquí
        if len(self.commands) >= 20:
            self.commands.pop()  # Elimina el último comando si se alcanza el límite de 20
        new_command = CommandHistoryModel(command) # Crear una nueva instancia de CommandHistoryModel
        self.commands.insert(0, new_command.get_command())  # Inserta el nuevo comando al principio de la lista
        self.save_to_json() 
        #presentando los comandos
        print("Comango agregado: ", new_command.get_command())
        print("Comandos: ", self.commands)

    #guardar json
    def save_to_json(self):
        file_path = os.path.join(data_folder, 'commands.json')
        with open(file_path, 'w') as file:
            json.dump(self.commands, file)
    #cargar json-- metodo propio de JSON para guardar, leer 
    def load_from_json(self):
        file_path = os.path.join(data_folder, 'commands.json')
        try:
            with open(file_path, 'r') as file:
                commands = json.load(file)
                print("Comandos cargados: ", commands) # Convertir los diccionarios cargados a instancias de CommandHistoryModel
        except FileNotFoundError:
            commands = []
        return commands