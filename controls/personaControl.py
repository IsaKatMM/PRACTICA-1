from models.persona import Persona
from controls.tda.linked.linkedList import Linked_List

class PersonaControl:
    def __init__(self):
        self.__persona = None
        self.__lista = Linked_List()
        
    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
           self.__lista.add(self.__persona,self.__lista._length)