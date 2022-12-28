
print("Hola asi que quieres un nuevo telefono ")
pregunta=input( "IOS o Android :")

if pregunta == "android":
    dinero=input("Tienes dinero")

    if dinero == "no":
        print("android chino por $100")
    if dinero == "si":
        camara=input("te importa la camara? ")
        if camara =="si":
            print("GOOGLE PIXEL4")
        if camara =="no":
            print("Android calidad presio")

elif pregunta =="ios":
    dinero2=input("tienes dinero")
    if dinero2 =="si":
        print("iphon pro max")
    if dinero2 =="no":
        print("iphon de segunda")
""