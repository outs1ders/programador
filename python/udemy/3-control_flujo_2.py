#while
#i=1

#while i<5:
#    print(i)
#    i+=1

#stop while
#use break
#i=1

#while i<5:
#    print(i)
#    if i==3:
#        break
#    i+=1

#continue with execution
#i=1

#while i<5:
#    i+=1
#    if i==3:
#        continue
#    print(i)


#--------------------------------------------------

#for

usurios=["david", "julian", "fernando", "eduardo"]
for usuario in usurios:
    print(usuario)

string_1="la noche es bonita"
for letras in string_1:
    print(letras)

#stop for
#use break

usurios=["david", "julian", "fernando", "eduardo"]
for usuario in usurios:
    if usuario == "julian":
        break
    print(usuario)


#continue execution

usurios=["david", "julian", "fernando", "eduardo"]
for usuario in usurios:
    if usuario == "julian":
        continue
    print(usuario)

#range(x,y,z)   x=num.inicial , y=num.final,    z=aumento
for numero in range(3,20,3):
    print (numero)
else: #se puede agregar un else despues del for pararalizar una accion adicional despues de la iteracion
    print("ya ha acabado la iteracion")

#for anidado
usuarios=["david", "julian", "fernando", "eduardo"]
edades=[24, 25, 27, 30]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edades)