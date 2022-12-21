# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla
# el número de palabras que contiene.

import urllib.request

def read_url(url):
    file = urllib.request.urlopen(url)
    datos = file.read()
    print(len(datos.split()))
    return

url = "http://textfiles.com/adventure/aencounter.txt"
read_url(url)

