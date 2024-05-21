import enum
class EnumTipoIdentificacion(enum.Enum):
    
    CEDULA = 'CEDULA'
    PASAPORTE = 'PASAPORTE'
    RUC = 'RUC'


    def getValues(self):
        return self.value
    