#exercise_1
#   multiplica dos numeros sin usar el simbolo de multiplicacion
def multiplicacion(num1,num2):
    resul=0
    for x in range(num1):
        resul+=num2
    return resul

#print(multiplicacion(2,3))

#exercise_2
#   resive "nombre" y "apellido" e imprimelo al revez
nombre='Juan'
apellido = 'Feliz'

nombre_c=nombre + " " + apellido
#print(nombre_c[::-1])   # la instruccion [::-1] en una string la imprime al revez

#exercise_3
#   escribir una funcion que encuentre el menor numero  de un lista

list_numeros=[1,2,3,-4,-5,6]

menor="inicial"

for num in list_numeros:
    if menor == 'inicial':
        menor = num
    else:
        menor = num if num < menor else menor

#print(menor)

#exercise 4
#   escribir una funcion que devuelva el volumen de una esfera por su radio

def volumen(r):
    return 4/3 * 3.1416 * r ** 3

#print(volumen(3))

#exercise 5
#   escriba una funcion que indique si el usurio es mayor de edad

def mayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,edad):
        self.edad=edad

usuario=Usuario(15)
usuario_2=Usuario(20)

resultado_1=mayor(usuario)
resultado_2=mayor(usuario_2)

print(resultado_1,resultado_2)

#exercise 6
# escribe una funcion que indique si el numero es par o impar
def es_par(n):
    return n % 2 == 0

print(es_par(10))

#exercise 7
# escribe una funcion que indique cuantas volales tiene una palabra

# mi solucion
"""
def vocales_c(word):
    i=0
    vocales=["a","e","i","o","u"]
    word_l=word.lower()
    for letter in word_l:
        if letter in vocales:
            i+=1
    return i

print(vocales_c("hAbia Una vez UnA iguana"))
"""

# solucion del profesor

palabra="hAbia Una vez UnA iguana"
vocales=0
for y in palabra:
    x=y.lower()
    vocales +=1 if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" else 0

print(vocales)

#exercise 8
# escribir una aplicacion que reciba una cantidad de numeros infinita hata
# que se escriba la palabra "basta", y  tome todo los numeros y los sume
"""
list_numeros=[]

while True:
    ingreso=input("ingrese un numero, si ya acabo de ingresarlos difgite |basta|")
    if ingreso == "basta":
        break
    else:
        try:
            ingreso=int(ingreso)
            list_numeros.append(ingreso)
        except:
            ingreso="valor no permitido"
            exit()

resultado=0
for numero in list_numeros:
    resultado+=numero

print(resultado)
"""
#exercise 9
# escribir una funcion que reciba nombre y apellido y cree un archivo con los mismos
def nombre_y_apellido(nombre,apellido):
    c=open("nombre_full.txt", "a")
    c.write(nombre+' '+ apellido+'\n')
    c.close()

nombre_y_apellido("chachito", "feliz")