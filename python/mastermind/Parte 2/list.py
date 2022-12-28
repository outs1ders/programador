import os
lista_de_compra=[]

print("Programa lista de la compra")

agregado = None
while True:
    agregado=input("Que desea comprar? ([Q] para salir): ")

    if agregado == "Q":
        break

    elif agregado in lista_de_compra:
        print("Ya esta agregado")

    else:
        if input("seguro que desea añadir {}  |S| si |N| no :  ".format(agregado)) == "s" or "S":
            lista_de_compra.append(agregado)


    input("Presioneenter para continuar")
    os.system("cls")


print(lista_de_compra)

