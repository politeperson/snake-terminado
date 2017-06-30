#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored
from time import *
from os import system
def guardar_puntajes(nombre_archivo, puntajes):
    archivo = open(nombre_archivo, "a")
    for nombre , puntaje , fecha in puntajes:
        archivo.write(nombre+","+str(puntaje)+","+fecha+"\n")
    archivo.close()

def recuperar_puntaje(nombre_archivo):
    puntajes = []
    archivo = open(nombre_archivo,"r")
    for linea in archivo:
        nombre , puntaje , fecha = linea.rstrip("\n").split(",")
        puntajes.append([nombre , puntaje , fecha])
    archivo.close()
    return puntajes

def espera(n):
    print "espere..."
    sleep(n)
    system("clear")

def mostrar_puntajes():
    band = True
    ordenar = []
    recuperado = recuperar_puntaje("puntajes.txt")
    for i in range(0,len(recuperado) - 1):
        maxi = i
        for j in range(i + 1 , len(recuperado)):
            if int(recuperado[j][1]) > int(recuperado[maxi][1]):
                maxi = j
        if maxi != i:
            recuperado[i] , recuperado[maxi] = recuperado[maxi] , recuperado[i]
            
    while band:
        print colored("\t\t.:PUNTAJES:." , "yellow")
        print colored("Nombre\t\t Puntaje\t\tFecha" , "cyan")
        for i in range(len(recuperado)):
            for j in range(len(recuperado[i])):
                if j == 1:
                    k = len(recuperado[i][j])
                    while k < 11:
                        recuperado[i][j] += " "
                        k += 1
                else:
                    k = len(recuperado[i][j])
                    while k < 18:
                        recuperado[i][j] += " "
                        k += 1
                print recuperado[i][j] ,  
            print
        try:
            print
            salir = int(raw_input("Presiona 1 para salir: "))
            assert salir == 1
            band = False
            espera(1)
        except ValueError:
            print colored("error: Digita solo números","red")
            espera(2)
        except AssertionError:
            print colored("error: solo puedes escoger el 1","red")
            espera(2)
            
