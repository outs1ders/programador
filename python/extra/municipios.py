import csv

archivo = open("tabla.csv",encoding="UTF-8")

lector = csv.reader(archivo,delimiter=";")

listaCostes = []
listaTipos=[]

holi=[]

for fila in lector:
    holi.append(fila[3])
    if fila[2] == "Chia":
        if not (fila[3] in listaCostes):
            listaCostes.append(fila[3])
            if fila[4]=="casa":
                if not (fila[3] in listaTipos):
                    listaTipos.append(fila[3])


holi.remove("Precio")

listaCostes_2 = [int(costos) for costos in listaCostes]
holi_2 =  [int(costos) for costos in holi]

valores_finales = []

for i in listaCostes_2:
    for n in holi_2:
        if n >= i:
            if n not in valores_finales:
                valores_finales.append(n) 
            
print (valores_finales)


