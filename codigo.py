#!/usr/bin/env python
import xml.etree.ElementTree as ElementTree
import csv

cadena1 = []  # contendra los valores de todas las facturas separados cada uno en una lista
cadena2 = []  # contendra los campos de la cabecera(primera fila)

num = 0

with open('dato.csv', 'rb') as csvfile:
    next(csvfile)
    lectura = csv.reader(csvfile, delimiter=';', quotechar='|')  # leer el fichero csv y separar los valores correspond.
    while num < 1:
        for f in lectura:
            # print(f)
            cadena1.append(f)
            num += 1


with open('dato.csv', 'rb') as csvfile:
    lectura = csv.reader(csvfile, delimiter=';', quotechar='|') # leer el fichero csv y separar los campos correspond.
    for row in lectura:
        cadena2 += row
        break


for indice in range(0, 5):      # sustituir los campos [x],donde x es un campo de la cabecera por el correspond. valor

    fichero = open("plantilla", "rt")
    salida = open("factura"+str(indice+1)+".xml", "wt")

    for a in fichero:
        variable = 0
        for x in cadena2:
            if "[" + x + "]" in a:
                # print("["+x+"]")
                # print(cadena1[indice][cadena2.index(x)])
                a = a.replace("[" + x + "]", cadena1[indice][cadena2.index(x)])
                salida.write(a)
                variable = 1

        if variable == 0:
            salida.write(a)


    fichero.close   # cerrar el fichero creado y la plantilla aunque no es obligatorio hacerlo
    salida.close


