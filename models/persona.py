from models.enumTipoIdentificacion import EnumTipoIdentificacion
class Persona:
    def __init__(self):
        self.__id = 0
        self.__apellido = ""
        self.__nombre = ""
        self.__dni = ""
        self.__direccion = ""
        self.__telefono = ""
        self.__tipoIdentificacion = EnumTipoIdentificacion.CEDULA

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    def __str__(self) -> str:
        return self.__apellidos+" "+ self.__nombre
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellido": self.__apellido,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "dni": self.__dni,
            "telefono": self.__telefono,
            "tipo": self.__tipoIdentificacion
        }
        
    def deserializar(data): 
        persona = Persona()
        persona._id = data["id"]
        persona._apellido = data["apellido"]
        persona._nombre = data["nombre"]
        persona._direccion = data["direccion"]
        persona._dni = data["dni"]
        persona._telefono = data["telefono"]
        persona._tipoIdentificacion = data["tipo"]
        return persona