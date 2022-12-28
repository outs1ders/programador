#funcion "def"
def nme_complete():
    print("hola")

#def_matodo1
def imprimirdato(nombre):
    print("El nombre completo es: ", nombre)

#utilizamos una argumento al llamar a la funcion
#imprimirdato("perro")

#def_matodo2
def imprimirdato(*nombre): #usamos * para mas de un argumento
    print("El nombre completo es: ", nombre)

#imprimirdato("prro","gato","chanchito")

#def_metodo3
def nombrecompleto(apellido, nombre):
    print(nombre, apellido)

#nombrecompleto(nombre="chachito", apellido="feliz")

#def_metodo4
def nombreCompleto2(**kwargs): #**kwargs se utliza para que el argumento se use por la sintaxis de diccionario
    print(kwargs['nombre'],kwargs['apellido'])

#nombreCompleto2(nombre='chanchito',apellido='feliz')

#def with default argument
def funcion_1(argumento="chancho"):
    print(argumento)

#funcion_1()

#def with a list

def myfuntion_list(lista):
    for word in lista:
        print(word)

#myfuntion_list(["habia", "una", "vaz", "un", "niño"])

#def wiyh return
def myfuntion_list_2(lista):
    a=""
    for word in lista:
        a= a + word + " "
    return a

name=myfuntion_list_2(["habia", "una", "vaz", "un", "niño"])
print(name)