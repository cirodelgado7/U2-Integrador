import csv
from ClaseMedicamento import Medicamento


class MM:
    __lista_medicamentos = []

    def __init__(self):
        self.__lista_medicamentos = []

    def cargarArchivo(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                idCama = fila[0]
                idMedicamento = fila[1]
                nombreComercial = fila[2]
                monodroga = fila[3]
                presentacion = fila[4]
                cantidad = fila[5]
                precio = fila[6]
                unMedicamento = Medicamento(idCama, idMedicamento, nombreComercial, monodroga, presentacion, cantidad,
                                            precio)
                self.__lista_medicamentos.append(unMedicamento)
        archivo.close()

    def mostrar(self, indice):
        a = 0
        for i in range(len(self.__lista_medicamentos)):
            if self.__lista_medicamentos[i].getIdCama() == self.__lista_medicamentos[indice].getIdCama():
                print('{:28} {:22} {:13} {:20}'
                      .format(self.__lista_medicamentos[i].getNombreComercial(),
                              self.__lista_medicamentos[i].getPresentacion(),
                              self.__lista_medicamentos[i].getCantidad(),
                              self.__lista_medicamentos[i].getPrecio()))
                a += float(self.__lista_medicamentos[i].getPrecio())
        return a


    def getLongitud(self):
        return len(self.__lista_medicamentos)
