from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty
class StackOperation(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTope(self):
        print(self._length)
        return self._length < self.__tope
    
    
    def push(self, data):
        if self.verifyTope:
            self.add(data, 0)
        else:
            raise LinkedEmpty("Stack full")
        
    @property
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete(0)
    
    