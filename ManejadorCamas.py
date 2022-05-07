import numpy as np
import csv
from ClaseCama import Cama
import datetime


class MC:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__camas = np.empty(dimension, dtype=Cama)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = " "
        for lista in self.__camas:
            s += str(lista) + ' '
        return s + " "

    def agregarCama(self, unaCama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = unaCama
        self.__cantidad += 1

    def cargarArchivo(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                idCama = fila[0]
                habitacion = fila[1]
                estado = fila[2]
                nombre = fila[3]
                diagnostico = fila[4]
                fechaInternacion = fila[5]
                fechaAlta = fila[6]
                unaCama = Cama(idCama, habitacion, estado, nombre, diagnostico, fechaInternacion, fechaAlta)
                self.agregarCama(unaCama)
        archivo.close()

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__camas[i])

    def buscarCama(self, n, mm):
        i = 0
        while i < len(self.__camas):
            if self.__camas[i].getNombre() == n:
                self.darAlta(i, mm)
            i += 1

    def darAlta(self, i, mm):
        self.__camas[i].setFechaAlta('06/05/22')
        self.__camas[i].setEstado('False')
        if i < len(self.__camas):
            print('Paciente: {} \t\t Cama: {} \t\t Habitación: {}'
                  .format(self.__camas[i].getNombre(), self.__camas[i].getIdCama(), self.__camas[i].getHabitacion()))
            print('Diagníostico: {} \t\t Fecha de Internación: {}'
                  .format(self.__camas[i].getDiagnostico(), self.__camas[i].getFechaInternacion()))
            print('Fecha de ALta: {}'.format(self.__camas[i].getFechaAlta()))
        print('Medicamento/Monodroga \t\t Presentación \t\t Cantidad \t\t Precio')
        a = mm.mostrar(i)
        print('Total adeudado: {:56}'.format(a))

    def listarPaciente(self, d):
        for i in range(len(self.__camas)):
            if self.__camas[i].getDiagnostico() == d and self.__camas[i].getEstado() is not None:
                print('\nPaciente: {}\nCama: {}\nHabitación: {}\nFecha de Internación: {}'
                      .format(self.__camas[i].getNombre(), self.__camas[i].getIdCama(),
                              self.__camas[i].getHabitacion(), self.__camas[i].getFechaInternacion()))
