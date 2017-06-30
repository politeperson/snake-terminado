#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored
from juego import *
from Tkinter import *
from os import *
from pygame import *
from puntajes import *
from datetime import *

def sacar1(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][1]-1!=serp.posicion[len(serp.posicion)-2][1] and serp.direccion!="derecha":
        serp.direccion="izquierda"
def sacar2(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][1]+1!=serp.posicion[len(serp.posicion)-2][1] and serp.direccion!="izquierda":
        serp.direccion="derecha"
def sacar3(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][0]-1!=serp.posicion[len(serp.posicion)-2][0] and serp.direccion!="abajo":
        serp.direccion="arriba"
def sacar4(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][0]+1!=serp.posicion[len(serp.posicion)-2][0] and serp.direccion!="arriba":
        serp.direccion="abajo"
def salir(event):
    serp.puntaje = 0
    serp.total = 0
    serp.posicion = [[0,0],[0,1],[0,2]]
    serp.nivel = 1
    serp.estado = "perder"
    root.destroy()
    system("clear")

def task():
    global serp
    global space
    global manzana
    global dif
    global score
    
    sleep(serp.velocidad)
    if serp.estado=="ganar":
        return 0
    if movimiento(serp,space,manzana,dif)==False:
        system("clear")
        score = [[serp.jugador , serp.total , str(datetime.now())]]
        guardar_puntajes("puntajes.txt" , score)
        if serp.total >= 100:
            if serp.total >= 200:
                if serp.total >= 300:
                    print "Puntaje Total: ",serp.total
                    print "Eres muy bueno en esto"
                else:
                    print "Puntaje Total: ",serp.total
                    print "Lo estas haciendo genial"
            else:
                print "Puntaje Total: ",serp.total
                print "Sigue practicando te falta solo un poco mas"
        else:
            print "Puntaje Total: ",serp.total
            print "Perdiste :'("
        print "\n\t\tPresiona ESC para regresar al menu\n\n"
        return 0      
    root.after(10,task)

global serp
global space
space=espacio()
space.x=20
space.y=20
serp=serpiente()
serp.direccion="derecha"
serp.posicion=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
manzana=fruta()
dif=obstaculos()

def iniciar():
    global root
    root=Tk()
    root.after(1 , task)
    
    root.bind('<Left>',sacar1)
    root.bind('<Right>',sacar2)
    root.bind('<Up>',sacar3)
    root.bind('<Down>',sacar4)
    
    root.bind('<a>',sacar1)
    root.bind('<d>',sacar2)
    root.bind('<w>',sacar3)
    root.bind('<s>',sacar4)

    root.bind('<A>',sacar1)
    root.bind('<D>',sacar2)
    root.bind('<W>',sacar3)
    root.bind('<S>',sacar4)

    root.bind('<Escape>',salir)

    
    frame = Frame(root, width=100, height=100)
    frame.pack()

    root.title("Snake Configuration")
    
    root.mainloop()
    return root

def espera(n):
    print "espere..."
    sleep(n)
    system("clear")

def velocidad():
    opcion = 0
    band = True
    while band:
        print "\t\t.:Velocidad"
        print "1. Mínima"
        print "2. Media "
        print "3. Máxima "
        print "4. Atrás "
        try:
            opcion = int(raw_input("Opción: "))
            assert opcion >= 1 and opcion <= 4
        except ValueError:
            print "Porfavor digitar solo numeros"
            espera(2)
        except AssertionError:
            print "Digita solo los numeros de la lista"
            espera(2)
        else:
            if opcion == 1:
                serp.velocidad = 0.3
                print "Velocidad cambiada"
                espera(1)
            elif opcion == 2:
                serp.velocidad = 0.2
                print "Velocidad cambiada"
                espera(1)                
            elif opcion == 3:
                print "Velocidad cambiada"
                espera(1)    
                serp.velocidad = 0.1
            else:
                espera(1)
                snake()
    return

def snake_color():
    opcion = 0
    band = True
    while band:
        print "\t\t.:Color:."
        cprint("1. Red", "red")
        cprint("2. Green", "green")
        cprint("3. Yellow", "yellow")
        cprint("4. White", "white")
        cprint("5. Cyan", "cyan")
        cprint("6. Magenta", "magenta")
        cprint("7. Blue", "blue")
        cprint("8. Grey", "grey")
        print "9. Salir"
        try:
            opcion = int(raw_input("Opción: "))
            assert opcion >= 1 and opcion <= 9
        except ValueError:
            print "Porfavor digitar solo los numeros"
            espera(2)
        except AssertionError:
            print "Digita solo los numeros de la lista"
            espera(2)
        else:
            if opcion == 1:
                espera(1)
                serp.color = "red"
            elif opcion == 2:
                espera(1)
                serp.color = "green"
            elif opcion == 3:
                espera(1)
                serp.color = "yellow"
            elif opcion == 4:
                espera(1)
                serp.color = "white"
            elif opcion == 5:
                espera(1)
                serp.color = "cyan"
            elif opcion == 6:
                espera(1)
                serp.color = "magenta"
            elif opcion == 7:
                espera(1)
                serp.color = "blue"
            elif opcion == 8:
                espera(1)
                serp.color = "grey"
            else:
                espera(1)
                snake()
    return

def snake():
    opcion = 0
    band = True
    while band:
        print "\t\t.:Snake:."
        print "1. Velocidad"
        print "2. Forma "
        print "3. Color "
        print "4. Atrás "
        try:
            opcion = int(raw_input("Opción: "))
            assert opcion >= 1 and opcion <= 4
        except ValueError:
            print "Porfavor digitar solo los numeros"
            espera(2)
        except AssertionError:
            print "Digita solo los numeros de la lista"
            espera(2)
        else:
            if opcion == 1:
                espera(1)
                velocidad()
            elif opcion == 2:
                espera(1)
                bb = True
                while bb:
                    try:
                        forma = raw_input("Digita cualquier caracter: ")
                        assert len(forma) == 1
                    except AssertionError:
                        print "error: Solo puedes insertar un caracter: "
                        espera(2)
                    else:
                        espera(1)
                        serp.forma = forma
                        bb = False
            elif opcion == 3:
                espera(1)
                snake_color()
            else:
                espera(1)
                ajustes()
                
    return

def ajustes():
    opcion = 0
    elec = 0
    band = True
    while band:
        print "\t\t.:Ajustes:."
        print "1. Snake"
        print "2. Mapa "
        print "3. Music "
        print "4. Salir de Ajustes "
        try:
            opcion = int(raw_input("Opción: "))
            assert opcion >= 1 and opcion <= 4
        except ValueError:
            print "Porfavor digitar solo los numeros"
            espera(2)
        except AssertionError:
            print "Digita solo los numeros de la lista"
            espera(2)
        else:
            if opcion == 1:
                espera(1)
                snake()
            elif opcion  == 2:
                espera(1)
                print "Mínimo = 10 x 10"
                print "Máximo = 40 x 40"
                flag = True
                while flag:
                    try:
                        tam = int(raw_input("Tamaño N x N: "))
                        assert tam >= 10 and tam <= 40
                    except ValueError:
                        print "Digita solo números"
                        espera(2)                
                    except AssertionError:
                        print "error: escoge el tamaño dentro del rango especificado: "
                        espera(2)
                    else:
                        space.x = tam
                        space.y = tam
                        flag = False
                        espera(1)
            elif opcion == 3:
                espera(1)
                flag = True
                while flag:
                    cprint("♪♫ MUSIC ♫♪" , "cyan")
                    print "1. SI"
                    print "2. NO"
                    print "3. Salir"
                    try:
                        tam = int(raw_input("Opción: "))
                        assert tam >= 1 and tam <= 3
                    except ValueError:
                        print "Digita solo números"
                        espera(2)                
                    except AssertionError:
                        print "error: escoge solo una de las opciones"
                        espera(2)
                    else:
                        if tam == 1:
                            espera(1)
                            playMusic()
                            
                        elif tam == 2:
                            espera(1)
                            stopMusic()
                        else:
                            espera(1)
                            flag = False
                            ajustes()
            else:
                espera(1)
                band = False
                menu()
    return

def playMusic():
    mixer.init()
    mixer.music.load("Spy Hunter.mp3")
    mixer.music.play(-1)

def stopMusic():
    mixer.init()
    mixer.music.load("Spy Hunter.mp3")
    mixer.music.stop()
    
def menu():
    opcion = 0
    gg = 1
    band = True
    name = recuperar_puntaje("puntajes.txt")
    while band:
        print colored("\t\t\t.:BIENVENIDOO A SNAKE:.", "yellow"),
        print "\t\t\t" , serp.jugador
        print "1. Nuevo Juego"
        print "2. ¿Nuevo Jugador?" 
        print "3. Puntajes"
        print "4. Información"
        print "5. Ajustes"
        print "6. Salir"
        try:
            opcion = int(raw_input("Opción: "))
            assert opcion >= 1 and opcion <= 6
        except ValueError:
            print "\tPorfavor digitar solo los numeros"
            espera(2)
        except AssertionError:
            print "\tDigita solo los numeros de la lista"
            espera(2)
        else:
            if opcion == 1:
                cont=1
                system("clear")
                while(cont > 0):
                    print "el juego comienza en...",cont
                    sleep(1)
                    system("clear")
                    cont -= 1
                iniciar()
            elif opcion == 2:
                espera(1)
                nombre = raw_input("Digite su nombre de jugador: ")
                serp.jugador = nombre
                espera(1)
            elif opcion == 3:
                espera(1)
                mostrar_puntajes()
            elif opcion == 4:
                print "info"
                espera(1)
            elif opcion == 5:
                espera(1)
                ajustes()
            else:
                raise SystemExit
    return
#playMusic()
menu()

