from random import randint
import os

LIFE_PIKACHU_START = 90
LIFE_CHARMANDER_START = 80

TAMAÑO_BARRA_LIFE = 10


life_pikachu= LIFE_PIKACHU_START
life_charmander=LIFE_CHARMANDER_START


while life_charmander > 0 and life_pikachu > 0:
    # empiezan los combates

    # Turno de pikachu
    print("Turno de pikachu")

    ataque_pikachu= randint(1,4)
    if ataque_pikachu == 1:
        #Bola_voltio
        print("Pikachu ataca con vol voltio")
        life_charmander -= 30
    elif ataque_pikachu == 2:
        #impactrueno
        print("Pikachu ataca con impactrueno")
        life_charmander -= 30
    elif ataque_pikachu == 3:
        #ataque_rapido
        print("Pikachu ataca con ataque rapido")
        life_charmander -= 40


    if life_pikachu < 0:
        life_pikachu = 0
    if life_charmander < 0:
        life_charmander = 0

    #medidoires de vida
    medidor_vide_pikachu = int(life_pikachu * TAMAÑO_BARRA_LIFE  / LIFE_PIKACHU_START)
    medidor_vida_charmander = int(life_charmander * TAMAÑO_BARRA_LIFE  / LIFE_CHARMANDER_START)

    print("la vida de pikachu [{}{}] ({}/{})".format("*" * medidor_vide_pikachu,
            " " * (TAMAÑO_BARRA_LIFE  - medidor_vide_pikachu),life_pikachu, LIFE_PIKACHU_START))
    print("la vida de charmander [{}{}] ({}/{})".format("*" * medidor_vida_charmander,
            " " * (TAMAÑO_BARRA_LIFE  - medidor_vida_charmander), life_charmander,LIFE_CHARMANDER_START))
    input("ENTER para continuar  \n")

    if life_pikachu <= 0:
          break
    if life_charmander <= 0:
          break

    os.system("cls")

    #Turno_charmander
    print("Turno de charmander")


    ataque_charmander=None

    while ataque_charmander not in ["a","b","c"]:
        ataque_charmander= input("Que ataque va a realizar a| llamarada b| colmillo igneo c  ataque dragon: ")

    if ataque_charmander=="a":
        life_pikachu-=10
    elif ataque_charmander=="b":
        life_pikachu-=10
    elif ataque_charmander=="c":
        life_pikachu-=9

    if life_pikachu < 0:
        life_pikachu = 0
    if life_charmander < 0:
        life_charmander = 0

    #medidores de vida
    medidor_vide_pikachu = int(life_pikachu * TAMAÑO_BARRA_LIFE / LIFE_PIKACHU_START)
    medidor_vida_charmander = int(life_charmander * TAMAÑO_BARRA_LIFE/ LIFE_CHARMANDER_START)
    print("la vida de pikachu [{}{}] ({}/{})".format("*" * medidor_vide_pikachu,
                " " * (TAMAÑO_BARRA_LIFE  - medidor_vide_pikachu),life_pikachu, LIFE_PIKACHU_START))
    print("la vida de charmander [{}{}] ({}/{})".format("*" * medidor_vida_charmander
                ," " * (TAMAÑO_BARRA_LIFE  - medidor_vida_charmander), life_charmander,LIFE_CHARMANDER_START))

    if life_pikachu <= 0:
        break
    if life_charmander <= 0:
        break

    input("ENTER para continuar  \n\n")
    os.system("cls")

if life_pikachu > life_charmander:
    print("el ganador es pikachu")
else:
    print("el ganador es charmander")