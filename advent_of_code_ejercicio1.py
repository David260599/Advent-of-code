# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:05:23 2023

@author: David
"""
# Ejercicio 1 a
def suma_leer_numeros(ruta_fichero):
    suma = 0
    with open(ruta_fichero) as f:
        lineas = f.readlines()
        for linea in lineas:
            l = [string for string in linea if string.isdigit()]
            num = int(l[0] + l[-1])
            suma = suma + num
    return suma
#print(suma_leer_numeros("ejercicio1_advent_code.txt"))

# Ejercicio 1 b
from num2words import num2words

# Si estuvieran las palabras al completo sin solaparse
def suma_leer_numeros2(ruta_fichero):
    suma = 0
    lista_num_escritos = [[num,num2words(num)] for num in range(0,10)]
    dict_num_escritos = dict(lista_num_escritos)
    with open(ruta_fichero) as f:
        lineas = f.readlines()
        for linea in lineas:
            for key,value in dict_num_escritos.items():
                if value in linea:
                    linea = linea.replace(value, str(key))
            l = [string for string in linea if string.isdigit()]
            num = int(l[0] + l[-1])
            suma = suma + num
    return suma
print(suma_leer_numeros2("ejercicio1_advent_code.txt"))

# Si se solapan
    
def suma_leer_numeros2b(ruta_fichero):
    lista_num_escritos = [[num,num2words(num)] for num in range(0,10)]
    dict_num_escritos = dict(lista_num_escritos)
    suma = 0
    with open(ruta_fichero) as f:
        lineas = f.readlines()
        for linea in lineas:
            palabra = ""
            l = []
            encontrado = False
            for x in linea:
                if x.isdigit():
                    palabra = ""
                    l.append(int(x))
                    break
                else:
                    palabra = palabra + x
                    for key, value in dict_num_escritos.items():
                        if palabra.find(value) >= 0:
                            l.append(key)
                            palabra = ""
                            encontrado = True
                    if encontrado == True:
                        break  
            encontrado = False
            for x in linea[::-1]:
                if x.isdigit():
                    palabra = ""
                    l.append(int(x))
                    break
                else:
                    palabra = palabra + x
                    for key, value in dict_num_escritos.items():
                        if palabra[::-1].find(value) >= 0:
                            l.append(key)
                            palabra = ""
                            encontrado = True
                    if encontrado == True:
                        break  
            num = int(str(l[0]) + str(l[-1]))
            suma = suma + num
    return suma
print(suma_leer_numeros2b("ejercicio1_advent_code.txt"))
