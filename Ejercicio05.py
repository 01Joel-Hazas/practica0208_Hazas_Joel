# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
# ( https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true ),
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

import urllib.request

dict_pibs = {}
dict_pais = {}

def read_url(url):
    file = urllib.request.urlopen(url)
    datos = file.read().decode('utf-8').split('\n')
    años = datos.pop(0).split('\t')[1:]

    for pais in datos:
        datos_pais = pais.split('\t')
        codigo_pais = datos_pais.pop(0)[-2:]

        for i in range(len(datos_pais)):
            dict_pais[años[i].strip()] = datos_pais[i].strip()
        dict_pibs[codigo_pais] = dict_pais
    return dict_pibs

def mostrarPib(pibs, pais):
    for i, j in pibs[pais].items():
        print("Año:",i, "->" , '\t', j)

pais = input('Introduce el código de un país: ')
print('PIB per cápita de', pais)
mostrarPib(read_url("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)
