age=int(input("tell me your age: "))
carttype=input("tell me what type of cart do you have? (E estudent/P pensioner/F family/N nothing)")

if (25<= age >=35 and carttype== "E") or age<=10 or (age >= 65 and carttype== "P")or(carttype == "F"):
    print("se aplica el descuento")
else:
    print("no se aplica el descuento") 