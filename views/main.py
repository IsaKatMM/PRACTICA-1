import sys
sys.path.append('../')

from controls.tda.stack.stack import Stack
from controls.tda.queque.queque import Queque

stack = Stack(4)
queque = Queque(4)
try:
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    stack.print()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()
    
    queque.queque(1)
    queque.queque(2)
    queque.queque(3)
    queque.queque(4)    
    queque.print()
    queque.dequeque()
    queque.print()
except Exception as error:
    print("Errores")
    print(error)

'''
pc = PersonaControl()
pcb = PersonaDaoControl()
cd = CensoDao()

try:
    pc._persona._apellido = "Jimenez"
    pc._persona._nombre = "Juan"
    pc._persona._telefono = "123456"
    pc.save
    pcb._persona._apellido = "Gomez"
    pcb._persona._nombre = "Maria"
    pcb._persona._telefono = "654321"
    pcb.save
    pcb.__persona = None
    
    pc._persona._apellido = "Gonzalez"
    pc._persona._nombre = "Pedro"
    pc._persona._telefono = "987654"
    pcb._persona._apellido = "Guarnizo"
    pcb._persona._nombre = "Luis"
    pcb._persona._telefono = "456789"
    pc.save
    pcb.save
    
    cd.get_censo()._fecha = "2021-10-10"
    cd.get_censo()._censador = "Juan"
    cd.get_censo()._peso = 10.5
    cd.get_censo()._estatura = 1.5
    cd.save
    pcb.save
    
except Exception as error:
    print("Errores")
    print(error)'''