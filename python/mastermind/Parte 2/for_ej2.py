# --------------------------- Option 1--------------------------------------
"""
ingreso_numeros= input("ingrese los numeros separados por ,")
lista_numeros=ingreso_numeros.split(",")
numeros_limpios=[]

for numeros in lista_numeros:
    numeros_limpios.append(int(numeros))
"""
# ----------------------------option 2 -------------------------------------
"""
ingreso_numeros = input("ingrese los numeros serados por coma: ")
lista_numeros= ingreso_numeros.split(",")
lista_numeros= [int(numero) for numero in lista_numeros]
"""
# ----------------------------option 3 -------------------------------------
ingreso_de_nuemeros = input("ingrese los numeros separados por [,] : ")
lista_numeros = [int(numero) for numero in ingreso_de_nuemeros.split(",")]

number_small = lista_numeros[0]
number_big = lista_numeros[0]
# ---------------------------------------------------------------------------
for numero in lista_numeros:
    if number_small > numero:
        number_small = numero

    if number_big < numero:
        number_big = numero

print("El numero mas pequenño es : {} \nEl numero mas grande es : {} ".format(number_small,number_big))

