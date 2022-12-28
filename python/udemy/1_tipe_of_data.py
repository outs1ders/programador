# tambien usamos str()
string_2='palabaras'
string_1="oraciones"

#type of numbers

#enteros int()
entero=20

#decimal float()
decimal=20.5

#complejo
complejo=1j

#------------------------------------------------------------

#list
list=[1,2,4,]

#add to the list
#list.append(1)

#eliminate elements of the list
#list.clear

#copy the list
#ls=list.copy

#count the elements in the list
#list.count(3) #the element is so often 'el elemento esta tantas veces'

#elemts in a list
#len(list)

#acces the elemtes in a list
#list[1] # [numer of element] 0,1,2...~

#remove the lastest element of a list
#list.pop()

#remove the element of a list
#list.remove()

#change the order of the list
#list.reverse() # la lista queda ala inversa

#list.sort() #not use with string and int in the same list

#search the element in the list
#list.index() # (el elemento que se encuentra en la lista)

#range of the list
#range(list)

#----------------------------------------------------------

#tuplas
tupla=("hola","mundo","somos") # no son modificables

#search the element in the tupla
#tupla.index() #(el elemento que se encuentra en la lista)

#range of the tupla
#range(tupla)

#----------------------------------------------------------

#diccionary # el orden se determina por strings
#form1
diccionario={
    "nombre":"lulu",
    "edad":6,
    "raza":"criolla"
}

#form2
diccionario_=dict(nombre="lulu", edad="6", raza="criolla")


# formas de llamar un elemento
#   1. diccionario["elemento"]
#   2. diccionario.get("elemento")

#agregar al diccionario
#diccionario["value"]=element

#change the value of an element
#diccionario["elemento"]="larry"

#remove an element
#diccionario.pop("value")
#del diccionario["value"]

#remove the lastest element
#diccionario.popitem

#copy dictionary
#diccionario_2=diccionario.copy()
#dicionario_2=dict(diccionario)

#delate elements in a dictionary
#diccionario.clear()

#diccionario anidado
gatos={
    "lulu":{
        "nombre":"lulu",
        "edad":"seis"
    },
    "flurflix":{
        "nombre":"flurflix",
        "edad":"uno"
    }
}

#--------------------------------------------------

#booleanos

#true
verdader=True

#false
falso=False