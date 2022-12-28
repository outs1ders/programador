import random

titulo= "Juego del laberinto\n"
print(titulo+"_"*len(titulo)+"\n")

print(" Un dia sales de casa y vas en busca de aventuras ,recorres el mundo en busca de ella y de repente vez\n"
      "EL LABERINTO una colosal estructura llena de peligros a los cuales lagente advierte que si entras no volver\n"
      "a entrar pero si llegas al centro obtendras un deseo unico el cual te brindar todo lo que deseas sin exepciones\n"
      "y sin concecuencias.... ¿ aceptas el reto ?\n")

opcion=input("\n opcion[A] - aceptas | opcion [B] - no haceptas el reto \n")

if opcion == "a" and "A":
   print(" entras en el laberinto y vez un camino para seguir y un hombre te pregunta si estas seguro de entrar\n")
   opcion= input("opcion [a] - si | opcion [b] no")
   if opcion=="a"and "A":
        print("Llegas a una una rampa donde salen ratas muy extrañas y al parece venenosas y tienes dos opciones huir\n "
              "y seguir por ese camino o tratar de devolverte lo mas rapido posible\n")
        opcion=input("\n opcion[a] - siguir y correr | opcion [b] - buscas otra forma de escapar \n")

        if opcion == "a" and "A":
            print("sales corriendo hacia el camino de la derecha pero te quedas enserrado son las ratas o tu\n "
                  "¿Que haces peleas o buscas otra forma de escapar?\n")
            opcion=input("\n opcion[a] - pelear | opcion [b] - buscas otra forma de escapar \n")

            veneno = False

            if opcion== "a" and "A":
                print("con todas tus fuerzas peleas y sales victorioso ya que al correr tuviste mas campo para poder\n"
                      "atacar una por una pero una de las ratas te modio y ahora estas envenenado y si no llegas\n "
                      "rapido al centro moriras..... en ese momento se te habren dos caminos cada uno con un nombre;\n"
                      "el bien y el mal ¿cual elijes?\n")
                print("estas envenenado")

                veneno=True

                opcion=input("\n opcion[a] - el bien | opcion [b] - el mal \n")

                if opcion == "a" and "A":
                    print("Encuentras a un hombre anciano que te hace una pregunta .....¿Puedes respneder este dilema?\n"
                          "y si lo haces te ayudare...tines dos opciones decirle que no y seguir por el pasillo\n "
                          "o ayudarle")
                    opcion=input("\n opcion[a] - decir no | opcion [b] - ayudarle \n")

                    if opcion == "a"and "A":
                        print("El anciano se rie a lo lejos y escuchas que algo se abre en ese momento una compuerta\n "
                              "te hace caer y mueres de na forma horrible...FIN\n")

                    elif opcion == "b" and "B":
                        print("El anciano te pregunta ¿Que tan bueno crees para para elejir el bien?....tienes dos \n"
                              "opciones decir que eres bueno o decir que no eres bueno\n")
                        opcion=input("\n opcion[a] - soy bueno | opcion [b] - no soy bueno \n")

                        if opcion == "a"and "A":
                            print(" El anciano te dice que odia a los mentirosos....y se combierte en una especie \n"
                                  "montruo ye te come....y mueres de una muerte horrible\n")

                        elif opcion == "b"and "B":
                            print("El anciano aprecia tu sinceridad y se te abre un pasadiso que te lleva al centro\ "
                                  "del laberinto donde y pides tu deseo....FIN\n")
                        else:
                            print("nos has elejido opcion y has muerto")
                elif opcion == "b" and "B":
                    print("Entras y encuentras un pasillo vacio con una fuente en el medio y escuchas una voz \n"
                          "angelical que te dice que bebas el agua....tienes dos opciones beberla o no\n")
                    opcion=input("\n opcion[a] - bebes el agua | opcion [b] - no bebes e agua \n")

                    print("cuando la bebes te sientes mejor y si estas envenenado te curas .....si no lo estas \n"
                          "empiezas a alucinar poco a poco y te aparecen un ultimo camino hacia en final de laverinto\n"
                          " pero la voz te trata de convencer de quedarte\n")

                    if opcion == "a"and "A"and veneno==True:
                        print("Te curas del envenenamiento  y avanzas por un pasillo que se acaba de abrir despues de\n "
                              "un pequqño sismo y llegas al final del laberinto y ganas....FIN \n")

                    elif opcion == "a" and "A" and veneno ==False:
                        print("empiezas a alusinar lentamente mientras que caminas y aquella voz angelical te\n "
                              "convence de quedarte mientras que te vuelves mas y mas loco , hasta que con el \n"
                              "tiempo mueres....FIN \n")

                    elif opcion == "b" and "B":
                        print("decides seguir por tu camino por el unico pasadiso que encuentras pero al llegar a el\n "
                              "se cierra el cuarto de la fuente y quedas atrapado en el laberino sin poder escapar\n "
                              " despues de un tiempo mueres de hambre....FIN\n")
                    else:
                        print("nos has elejido opcion y has muerto")
                else:
                    print("nos has elejido opcion y has muerto")

            elif opcion =="b" and "B":
                print(" sales corriendo con todo lo que puedes y por fin vez una puerte algo pequeña y entras, al\n"
                      " entrar vez un monton de nomos los cuales te dicen que si quieres su ayuda te la daran si \n"
                      "respondes el siguiente problema....30 veces un numero aleatorio mas 6 -7 ser tu igual tienes\n"
                      " dos opciones, responder o no responder \n")
                opcion= input("opcion[a] - responder | opcion[b] - no responder\n")


                if opcion == "a" and "A":
                    nuemeroaleatrio = random.randint(10, 300)
                    print("responde 30* {}+7-6".format(nuemeroaleatrio))
                    respuesta= input()



                    if respuesta == 30 * nuemeroaleatrio +7-6:
                         print("Eres asesinado y comido por los nomos porque dicen que odian a los sabelotodos y \n "
                               "mueres de una forma horrible....FIN\n")

                    else:
                        print("Dicen que eres un tonto y se compadecen de ti ydeciden ayudarte a llegar al final del\n "
                              "laberinto con la condicion de que tu deseo los beneficie....tienes dos opciones\n "
                              "aceptar o no\n"
                              "")
                        opcion=input("opcion[a] - aceptas | opcion[b] - no aceptas ")

                        if opcion == "a" and "A":
                            print("te muestran una puerta,en la cual entras y vez una fuente en el medio y escuchas"
                                  " una voz angelical que te dice que bebas el agua....tienes dos opciones "
                                  "beberla o no \n")
                            opcion = input("\n opcion[a] - bebes el agua | opcion [b] - no bebes e agua \n")

                            print(
                                "cuando la bebes te sientes mejor y si estas envenenado te curas .....si no lo estas \n"
                                "empiezas a alucinar poco a poco y te aparecen un ultimo camino hacia en final de \n "
                                "laverinto pero la voz te trata de convencer de quedarte\n")

                            if opcion == "a" and "A" and veneno == True:
                                print(
                                    "Te curas del envenenamiento  y avanzas por un pasillo que se acaba de abri\nr "
                                    "despues de un pequqño sismo y llegas al final del laberinto y ganas....FIN \n")


                            elif opcion == "a" and "A" and veneno == False:
                                print(
                                      "empiezas a alusinar lentamente mientras que caminas y aquella voz angelical te\n "
                                    "convence de quedarte mientras que te vuelves mas y mas loco , hasta que con el \n"
                                    "tiempo mueres....FIN \n")

                            elif opcion == "b" and "B":
                                print(
                                    "decides seguir por tu camino por el unico pasadiso que encuentras pero al \n "
                                    "llegar a el, se cierra el cuarto de la fuente y quedas atrapado en el laberino \n"
                                    "sin poder escapar despues de un tiempo mueres de hambre....FIN\n")
                            gbelse:
                                print("nos has elejido opcion y has muerto")

                        elif opcion == "b" and "B":
                            print("los nomos pierden su compasion y deciden atacarte y matarte por ser egoista, \n "
                                  "mueres de una forma horrible comido vivo\n")
                        else:
                            print("nos has elejido opcion y has muerto")

                elif opcion== "b"and "B":
                    print("Los nomos se molestan y te atacan pero te dejan vivo para que sigas tu camino aunque muy\n "
                          "lastimado y lentamente asercandte a la muerte tienes dos opciones seguir con tu aventura\n"
                          " o buscar la salida\n")
                    opcion = input("opcion [a] -sigues con tu camino | opcion [b] -buscar una salida\n")

                    if opcion == "a"and "A":
                        print("sigues por un pasillo y lentamente vas atrallendo la atencion de seres parecidos a los\n"
                              "vampiros y desiden atacarte, mueres desangrado y en profunda agonia .......FIN\n")

                    elif opcion == "b"and "B":
                        print("Intentas buscar la salida sin exito y en poco tiempo a causa de tus eridas te desmayas\n"
                              "y mueres......FIN\n")

                    else:
                        print("nos has elejido opcion y has muerto")
            else:
                print("nos has elejido opcion y has muerto")

        elif opcion =="b" and "B":
            print("cuando trtas de devolverte el pasillo se cierra por todos lados y quedas atrapado junto con las\n"
                  " ratas y de repente vez una forma de trepar la pared ....y te encuentras con dos opciones \n"
                  "pelear o trepar")
            opcion = input("opcion [a] - pelear |opcion [b] trepar")

            if opcion == "a"and"A":
                print("Las ratas te superan en numero pero eres capas de vencelas y al final quedas muy herido y \n"
                      "sin forma de escapar y con el tiempo mueres devido al veneno y heridas\n")

            elif opcion == "b"and"B":
                print("Empiezas a trepar rapidamentey llegas a la sima donde vez como el laberinto cambia por cada\n "
                      "desicion que tomas y en ese momento se escucha una vos quedice.... TRAMPA......y te hace caer\n "
                      "en un lugar oscuro parecido a una tumba donde tienes dos opcines entrar por una pequeña puerta\n"
                      "que vez o tratar de buscar otro camino\n")
                opcion= input("opcion [a] - la puerta | opcion [b] -buscar otro camino\n ")

                if opcion == "a"and "A":
                    print("aparece un hombre grotesco y putrefacto que te dice ......tramposo, tramposo ,!!tramposo\n"
                          "con intencion de asesinarte y tienes dos opciones pelear o tratar de huir\n")
                    opcion = input( "opcion [a] - pelear [b] -tratar de huir\n")

                    if opcion == "a"and "A":
                        print("la pelea es muy igualada y los dos ya estan muy mal mal asi que vez dos armas a tu\n "
                              "disposicion una pistola antigua y una daga\n")
                        opcion = input("opcion [a] - pistola | opcion [b] - daga\n")

                        if opcion == "a"and"A":
                            print("la pistola sorpresibamente esta cargada y le das un tiro qque lo mata al instante\n"
                                  "en ese momento se abre un camino y llegas al centro del laberinto listo para \n"
                                  "recibir tu premio.......ganas .....FIN\n")

                        elif opcion == "b"and"B":
                            print("El hombre te ataca y resibe un gran corte pero con sus ultimos alientos te apuñala\n"
                                  "con en y mueres desangrado en el piso......FIN\n")

                    elif opcion == "b"and"B":
                        print("tratas de huir por la puerta pero esta cerrada y aquel hombre te ataca y asesina de una\n"
                              "forma horrible .......FIN\n")

                elif opcion == "b"and "B":
                    print("Buscas otro camino y despues de un tiempo encuentras un pasadiso secreto, donde entras\n"
                          "en un lugar donde se podia ver el centro del laberinto y una pasadiso dende dice que si \n"
                          "vienes podras salir de el tienes dos opciones seguir hacia el centro del laberinto o salir\n"
                          "y no arriesgarte\n")
                    opcion=input("opcion [a] - ir hacia el centro | opcion [b] - salir\n")

                    if opcion == "a"and "A":
                        print("tratas de ir pero no puedes llegar y con el tiempo te das cuenta que era una ilusion\n"
                              "antes de morir despues de que ha pasado un gran tiempo.....FIN\n")
                    elif opcion == "b" and "B":
                        print("pasa un buen tiempo llendo hacia la salida y cuendo te das cuentas estas en el centro\n"
                              ".....fin\n")
        else:
            print("nos has elejido opcion y has muerto")

   elif opcion == "b"and "B":
       print("te das de cuenta que no vale la pena y te vas de ahi")
   else:
       print("nos has elejido opcion y has muerto")