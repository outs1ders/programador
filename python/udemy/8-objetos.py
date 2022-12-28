#clases

class Usuario:  #siempre la instancia la primera en mayuscula example= Usuario
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def saludo(self): #ppor comodididad se utiliza self pero puede ser rempazado por alguna otro metodo
        print("buenas, bienvenido usurio", self.nombre, self.apellido)

#usuario =  Usuario("felipe", "feliz")
#usuario_2 = Usuario("chachito", "feliz")

#usuario.saludo()
#usuario.nombre="chanchito"
#usuario.saludo()

# del para eliminar un metodo o un ona definicion de objeto
#del usuario.nombre
#del usuario

# Herencia
class Admin(Usuario):   #tomammos los parametros y ibjetos de un clase anterior y la tomamos como una clase padre
    def super_saludo(self):
        print("hola soy", self.nombre, "y son un admin")

#admin= Admin("David","Feliz")   #definimos ls parametros al igual que en la clase anterior
#admin.saludo()  #podemos utilizar los mismos parametros de la clase padre
#admin.super_saludo()
#"usuario.super_saludo()" no podemos utlizar los parametros de la clase hijo

#Exersice 1

class Animal:
    def __init__(self, nombre, onomatopella):
        self.nombre=nombre
        self.onomatopella=onomatopella

    def saludo(self):
        print("Hola soy un", self.tipo, "y mi sonido es", self.onomatopella )
class Gato(Animal):
    tipo="gato"
    #extend init -- metodo1

    def __init__(self, nombre, onomatopella):
        Animal.__init__(self, nombre, onomatopella)
        print("Hi i am a cat, bilingual")

class Perro(Animal):
    tipo="perro"

    #exten init -- metodo2
    def __init__(self, nombre, onomatopella):
        super().__init__(nombre, onomatopella)
        
class Pajaro(Animal):
    tipo="pajaro"


gato=Gato("flurflis", "maullido")
perro=Perro("firulais", "ladrido")
pajaro=Pajaro("piolin","pitido")

gato.saludo()
perro.saludo()
pajaro.saludo()