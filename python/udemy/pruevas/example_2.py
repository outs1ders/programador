def imprimir_tabla(valores):
    
    for y in range (1,51):
        resultado = y * valores
        print (valores,"X",y,"=",resultado )
    return y

a=int(input("Ingrese un Número: "))
imprimir_tabla(a)
