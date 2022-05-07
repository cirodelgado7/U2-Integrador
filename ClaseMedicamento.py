class Medicamento:
    __idCama = ''
    __idMedicamento = 0
    __nombreComercial = ''
    __monodroga = ''
    __presentacion = ''
    __cantidad = ''
    __precio = ''

    def __init__(self, idCama, idMedicamento, nombreComercial, monodroga, presentacion, cantidad, precio):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreComercial = nombreComercial
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidad = cantidad
        self.__precio = precio

    def __str__(self):
        return '\n idCama: ' + self.__idCama + '\n Medicamento: ' + self.__idMedicamento + \
               '\n Nombre Comercial: ' + self.__nombreComercial + '\n Monodroga: ' + self.__monodroga + \
               '\n Presentación: ' + self.__presentacion + '\n Cantidad: ' + self.__cantidad + \
               '\n Precio: ' + self.__precio

    def getIdCama(self):
        return self.__idCama

    def getNombreComercial(self):
        return self.__nombreComercial

    def getPresentacion(self):
        return self.__presentacion

    def getCantidad(self):
        return self.__cantidad

    def getPrecio(self):
        return self.__precio
