# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
# la tabla de multiplicar de ese número, done n es el número introducido.

def tablas_mult(num):
    archivo = 'tabla-' + str(num) + '.txt'
    file = open(archivo, 'w')
    for i in range(1, 11):
        file.write(str(num) + ' x ' + str(i) + ' = ' + str(num * i) + '\n')
    file.close()

num = int(input('Introduce un número entero entre 1 y 10: '))
tablas_mult(num)
