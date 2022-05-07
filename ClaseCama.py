class Cama:
    __idCama = 0
    __habitacion = ''
    __estado = ''
    __nombre = ''
    __diagnostico = ''
    __fechaInternacion = ''
    __fechaAlta = ''

    def __init__(self, idCama, habitacion, estado, nombre, diagnostico, fechaInternacion, fechaAlta):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__nombre = nombre
        self.__diagnostico = diagnostico
        self.__fechaInternacion = fechaInternacion
        self.__fechaAlta = fechaAlta

    def __str__(self):
        return '\n\nidCama: ' + self.__idCama + '\nHabitación: ' + self.__habitacion + \
               '\nEstado: ' + self.__estado + '\nNombre: ' + self.__nombre + \
               '\nDiagnóstico: ' + self.__diagnostico + '\nFecha de Internación: ' + self.__fechaInternacion + \
               '\nFecha de Alta: ' + self.__fechaAlta

    def getIdCama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado

    def setEstado(self, e):
        self.__estado = e

    def getNombre(self):
        return self.__nombre

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaInternacion(self):
        return self.__fechaInternacion

    def getFechaAlta(self):
        return self.__fechaAlta

    def setFechaAlta(self, fecha):
        self.__fechaAlta = fecha
