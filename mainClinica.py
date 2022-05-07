from ManejadorCamas import MC
from ManejadorMedicamentos import MM


def test(mc, mm):
    n = input('\nNombre del Paciente: ')
    mc.buscarCama(n, mm)
    d = input('\n Diagnóstico: ')
    mc.listarPaciente(d)


if __name__ == '__main__':
    mc = MC(3, 5)
    mm = MM()
    mc.cargarArchivo()
    mm.cargarArchivo()
    test(mc, mm)
