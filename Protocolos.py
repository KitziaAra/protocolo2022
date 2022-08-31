from cgitb import text
from typing import TextIO


protocolo = []

def añadir1():
    i = int(input("Inserte el numero del paso "))
    texto= input("Inserte la instrucción: ")
    text = str(i)+ " " + texto
    protocolo.append(text)

def añadir2():
    i = int(input("Inserte el numero del paso"))
    j = input("Inserte el numero del subpaso a añadir: ")
    
#    x = int(protocolo.index(i)) +1 
    texto = input("Inserte la instrucción: ")
    text = str(j) + " " + texto
    protocolo.insert(i, text)

def borrar():
    for i in range(0,len(protocolo)):
        print(protocolo[i])
    j = int(input("Ingrese el indice de instrucción a borrar: "))

    protocolo.pop(j)

def modif():
    for i in range(0,len(protocolo)):
        print(protocolo[i])
    j = int(input("Ingrese el indice de instrucción a borrar: "))

    protocolo.pop(j)

    print("Ingrese la nueva instrucción y su numeración")
    texto = input("")
    protocolo.insert(j, texto)

def mostrar():
    for i in range(0,len(protocolo)):
        print(protocolo[i])

opc = "s"
while opc == "si" or opc == "s":
    print("CREAR PROTOCOLOS")
    print(" -menu- ")
    print("\t1- Añadir paso")
    print("\t2- Añadir subpaso")
    print("\t3- Borrar")
    print("\t4- Modificar")
    print("\t5- Ver protocolo")
    
    accion = int(input("¿Qué desea realizar?"))
    
    if accion == 1:
        añadir1()
    elif accion == 2:
        añadir2()
    elif accion == 3:
        borrar()
    elif accion == 4:
        modif()
    elif accion == 5:
        mostrar()
    else:
        print("Ingrese un valor válido")
    
    opc = input("Desea realizar algo más?")

print("Hasta luego")