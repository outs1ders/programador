
#Ejercicio 1
""""
texto_del_usurio= input("ingre alguna frase: ")
espacios = 0
puntos = 0
comas = 0

for frase in texto_del_usurio:
    if frase == " ":
        espacios += 1
    elif frase == ".":
        puntos +=1
    elif frase == ",":
        comas += 1

print("espacios: {} \npuntos : {} \ncomas: {}".format(espacios,puntos,comas))


#Ejercicio 2

texto_del_usurio = input("Ingrese un texto")
Mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","Ñ","O","P","Q","R","S","T","V","W","X","Y","Z"]
Numero_mayusculas = 0
for letras in texto_del_usurio:
    if letras in Mayusculas:
        Numero_mayusculas +=1

print("el numero de mayusculas es {}".format(Numero_mayusculas))

"""

#Ejercicio_3

nuemro_elegido= int(input("Ingrese un numero: "))

for numero in range(1,11):
    if numero % 4 == 0:  # Funciona como el mod de visual
        print("{} X {} = {}".format(nuemro_elegido,numero, numero * nuemro_elegido))



