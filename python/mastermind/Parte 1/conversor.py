
d_e=0.82
e_l=0.91
d_l=0.74
e_d=1.22

opcion=input("¿Que divisa quieres cambiar ?\n"
             " dolar a euro (d_e)\n"
             " euro a libra (e_l)\n"
             " dolar a libra (d_l)\n"
             " euro a dolar (e_d)\n")
if opcion == "d_e":
    sol1= float(input("que cantidad quierecambiar: "))
    print("su cambio es : {}".format(sol1*0.82))

elif opcion == "e_l":
    sol2 = float(input("que cantidad quierecambiar: "))
    print("su cambio es : {}".format(sol2 * 0.91))

elif opcion == "d_l":
    sol3 = float(input("que cantidad quierecambiar: "))
    print("su cambio es : {}".format(sol3 * 0.74))

elif opcion == "e_d":
    sol4 = float(input("que cantidad quierecambiar: "))
    print("su cambio es : {}".format(sol4 * 1.22))