#input1

#dato=input("ingrse dato ")

#cosas=["lapiz", "gato", "parlante", "noche", "negro" ]

#if cosas.count(dato) > 0:
#    print("el dato esta en la lista: ", dato)
#else:
#    print("el dato no existe, lloremos juntos")

#---------------------------------------------------------------

#input2

#metodo1
"""
primero=input("ingrese el numero: ")
try:
    primero=int(primero)
except:
    primero="error"

segundo=input("ingrse unnumero: ")
try:
    segundo=int(segundo)
except:
    segundo="error"

if primero == "error" or segundo == "eror":
    print("has cometido un error, solo puedes colocar numeros")
else:
    print(primero + segundo)
"""
#metodo2

primero=input("ingrese el numero: ")
try:
    primero=int(primero)
except:
    primero="error"

if primero == "error":
    print("has cometido un error, solo peuedes ingresar numeros")
    exit()

segundo=input("ingrse unnumero: ")
try:
    segundo=int(segundo)
except:
    segundo="error"

if segundo == "error":
    print("has cometido un error, solo peuedes ingresar numeros")
    exit()

operacion=input("que operacion desea relizar |+| |-| |*| |/| :")

if operacion == "+":
    print(primero + segundo)
elif operacion == "-":
    print(primero - segundo)
elif operacion == "*":
    print(primero * segundo)
elif operacion == "/":
    print(primero / segundo)