# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar
# de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje
# por pantalla informando de ello.

import os.path

def tablas_mult(n,m):

    archivo = 'tabla-' + str(n) + '.txt'

    if os.path.isfile(archivo):
        file = open(archivo, 'r')
        file.read(m)
    else:
        print('No existe el fichero con la tabla del', n)

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce un número entero entre 1 y 10: '))
tablas_mult(n,m)