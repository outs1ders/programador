import random

numero_ganador=random.
numero_elegido= int(input("elije un numero al asar entre 1 y 15:"))

print("veremos si ganas")

if numero_elegido==numero_ganador:
    print("has ganado")

if numero_elegido >15:
    print("he que te has pasado")

if numero_elegido <1:
    print("he que es muy corto")

if numero_elegido != numero_ganador :
    print("el numero ganador era {}".format(numero_ganador))