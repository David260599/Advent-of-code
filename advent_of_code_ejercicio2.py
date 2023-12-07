# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:50:03 2023

@author: David
"""

import re


# Ejercicio 2 a
def check_color(string, r, g, b):
    true_false = False
    color_dict = {'red':r, 'green':g, 'blue':b}
    color = [x for x in string.split() if x in color_dict.keys()][0]
    number = [int(x) for x in string.split() if x.isdigit()][0]
    if number <= color_dict[color]:
        true_false = True
    return true_false
    

def suma_ids_games_posibles(ruta_fichero, r ,g , b):
    suma = 0
    with open(ruta_fichero) as f:
        lineas = f.readlines()
        for linea in lineas:
            id = [int(x) for x in linea.split(':')[0].split() if x.isdigit()][0]
            set_list = [x for x in linea.split(':')[1].split(';')]
            flag_suma = True
            for set_elements in set_list:
                l = [check_color(x,r,g,b) for x in set_elements.split(',')]
                if False in l:
                    flag_suma = False
                    break
            if flag_suma == True:
                suma = suma + id
    return suma

# print(suma_ids_games_posibles("ejercicio2_advent_code.txt",12,13,14))

# Ejercicio 2 b

def maximos_set (string):
    colors = ['red', 'green', 'blue']
    maximos = [0,0,0] # Tres huecos para red, green y blue
    for cubes in string.split(';'):
        for cube in cubes.split(','):
            number = [int(x) for x in cube.split() if x.isdigit()][0]
            for i in range(0,len(colors)):
                if cube.find(colors[i]) >= 0:
                    if maximos[i] < number:
                        maximos[i] = number
    return maximos
    

def suma_multiplicacion_menores_cubos_posibles(ruta_fichero):
    suma = 0
    with open(ruta_fichero) as f:
        lineas = f.readlines()
        for linea in lineas:
           maximos = maximos_set(linea.split(':')[1])
           multiplicacion = 1
           for x in maximos:
               multiplicacion = multiplicacion * x
           suma = suma + multiplicacion
    return suma

print(suma_multiplicacion_menores_cubos_posibles("ejercicio2_advent_code.txt"))
                
                