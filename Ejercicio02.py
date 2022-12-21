# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt
# con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello
import os.path


def tablas_mult(numero):
    if numero > 10 or numero < 1:
        print("El número introducido no es valido")

    archivo = 'tabla-' + str(numero) + '.txt'

    if os.path.isfile(archivo):
        file = open(archivo, 'r')
        file.read()
    else:
        print('No existe el fichero con la tabla del', numero)

numero = int(input('Introduce un número entero entre 1 y 10: '))
tablas_mult(numero)
