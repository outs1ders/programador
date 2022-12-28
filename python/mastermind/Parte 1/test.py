
tutulo=("ESTE ES EL TEST DEL CHOCOLATE\n"
      "\nbienvenido\n")

print(tutulo +"_"*len(tutulo)+"\n")

puntos=0

opcion1= input("pregunta 1\n"
               "  ¿Que haces cuando vez el chocolate?\n"
               " a. Te sorprender y quieres ir a por el\n"
               " b. Te parece rico y quieres un trozo\n"
               " c. No te emociona mucho pero te gustaria probar\n"
               " d. No te apetece y ni lo volteas a ver\n")
if opcion1 == "a":
    puntos += 15
elif opcion1 == "b":
    puntos += 10
elif opcion1 == "c":
    puntos +=5
elif opcion1 == "d":
    puntos +=0
else:
    print("No has elegido una de las opciones validas")
    exit()

opcion2= input("pregunta 2\n"
               "  ¿Cuan tas veces comes chocolate a la semana?\n"
               " a. Casi todos por no decir que todos\n"
               " b. Tres o cuatro pero a veces odrian ser mas\n"
               " c. Una o dos pero podrian ser aveces mas aveces menos\n"
               " d. Casi nunca \n")
if opcion2 == "a":
    puntos += 15
elif opcion2 == "b":
    puntos += 10
elif opcion2 == "c":
    puntos +=5
elif opcion2 == "d":
    puntos +=0

opcion3= input("pregunta 3\n"
               "  ¿Del uno al diez cuanto te gusta el chocolate?\n"
               " a. Un dies total...lo adoro\n"
               " b. Entre un siete y un ocho\n"
               " c. Mas o menos un cuatro o un tres\n"
               " d. Un uno o un dos depende el dia \n")
if opcion3 == "a":
    puntos += 15
elif opcion3 == "b":
    puntos += 10
elif opcion3 == "c":
    puntos +=5
elif opcion3 == "d":
    puntos +=0

if puntos >= 40:
    print("FELICIDADES AMAS EL CHOCOLATE")
elif puntos >=25:
    print("Te gusta en gran medida el chocolate ")
elif puntos >= 15:
    print("Te gusta un poco el chocolate")
elif puntos >=0:
    print("No te gusta el chocolate o te gusta muy muy poco")

print(puntos)


