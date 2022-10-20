__author__ = ' MARTOS LUDMILA '
# Buenos dias profe, se que no se podia hacer sola el TP pero me canse de insistirles a mis compañeros
# para que hagamos algo y nos responden a los intentos de contacto que he tratado de tener mediante
# nuestro grupo de wasap. No se si lo tenga en cuenta pero necesitaba decirselo.
# Saludos cordiales

import random

AS = "AS"
J = "J"
Q = "Q"
K = "K"
numeros = (AS, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
palos = "Corazones", "Diamantes", "Pica", "Treboles"
puntaje_crupier = puntaje_jugador = 0

# contadores, banderas, acumuladores
puntaje_crupier = puntaje_jugador = pozo = 0
naturalJug = naturalCrup = False
maximo = 100000
ganadorJugador = ganadorCrupier =  False
contador_jugadas = contador_gana_jugador = contador_gana_crupier = 0
porc_vic_jug = cont_gana_crupier = cont_may_pozo = mayor = cm = acum_apuestas = perd_mas_grande = 0
salioDosAS = salioUnAS = bandera_crup_AS = False

def menu():
    print("\x1b[1;32m"+"*" * 50)
    print("Seleccione su jugada:")
    print("1: Apostar")
    print("2: Jugar una Mano")
    print("3: Salir")
    print("*" * 50)

def jugada_inicial():
    print("\x1b[1;32m"+"Las primeras dos cartas que salieron del Jugador son: "
      "\x1b[1;33m"+"\n", carta1_jugador, "de", "'" + carta1_jugador_palo + "'", "y", carta2_jugador, "de", "'" + carta2_jugador_palo + "'")
    print("\x1b[1;32m"+"Las primera carta del Crupier es: "
      "\x1b[1;33m"+"\n", carta1_crupier, "de", "'" + carta1_crupier_palo + "'")

def puntaje_dos_cartas(carta1, carta2):
    puntaje = 0
     # Si sale un AS que sume 11 puntos
    if carta1 == "AS" and carta2 != "AS" or carta2 == "AS" and carta1 != "AS":
        puntaje += 11
    # Si las dos cartas son AS que solo sume 2 puntos
    if carta1 == "AS" and carta2 == "AS":
        puntaje += 2
    # Para que sume las cartas que son numeros
    if carta1 != "AS" and carta1 != "J" and carta1 != "Q" and carta1 != "K":
        puntaje += carta1
    if carta2 != "AS" and carta2 != "J" and carta2 != "Q" and carta2 != "K":
        puntaje += carta2
    # Si salen Figuras que sume 10 puntos
    if carta1 == "J" or carta1 == "Q" or carta1 == "K":
        puntaje += 10
    if carta2 == "J" or carta2 == "Q" or carta2 == "K":
        puntaje += 10
    return puntaje

def puntaje_una_carta(carta):
    puntaje = 0
    # Para que sume las cartas que son numeros
    if carta != "AS" and carta != "J" and carta != "Q" and carta != "K":
        puntaje += carta
    # Si salen Figuras que sume 10 puntos
    if carta == "J" or carta == "Q" or carta == "K":
        puntaje += 10
    return puntaje

def apostar(monto):
    pozo = 0
    pozo += monto
    while monto <= 0 or pozo > maximo:
        pozo -= monto
        monto = int(input("Error! Ingrese otro monto: "))
        pozo += monto
    return pozo

print("\x1b[1;31m"+"\t\t*** BIENVENIDO AL JUEGO DEL BLACKJACK 2.0 ***")

# solicitamos nombre del jugador
nombre_jugador = input("\x1b[1;39m"+"Ingrese su nombre de Jugador: ")
while nombre_jugador == "" or nombre_jugador == " ":
    nombre_jugador = input("Error! Ingrese su nombre: ")

# monto del pozo INICIAL
pozo = int(input("\x1b[1;39m"+"Ingrese el monto del pozo inicial (mayor a 0 y menor a 100000): "))
while pozo <= 0 or pozo > maximo:
    pozo = int(input("Error!!! Ingrese el monto del pozo inicial (mayor a 0 y menor a 100000):"))
    # 4) El monto máximo que llegó a tener el jugador en el pozo.
if pozo > cont_may_pozo:
    cont_may_pozo = pozo
menu()
print("\x1b[1;39m")
op = int(input("Opcion seleccionada: "))
while op != 4:
    if op == 1:
        # esta opcion es para agregar plata al pozo que no supere maximo
        monto = int(input("Ingrese el monto a sumar al pozo: "))
        pozo += apostar(monto)

        if pozo > cont_may_pozo:
            cont_may_pozo = pozo
        print("\x1b[1;39m"+"POZO ACTUAL DEL JUGADOR", pozo)
        menu()
        op = int(input("Opcion seleccionada: "))

    if op == 2:
        if pozo < 5:
            print("\x1b[1;33m")
            opc = int(input("Su pozo es muy bajo...desea ingresar mas dinero? (1 = si, 2 = no ): "))
            if opc == 1:
                monto = int(input("Ingrese el monto a sumar al pozo: "))
                pozo += apostar(monto)
                if pozo > cont_may_pozo:
                    cont_may_pozo = pozo
        if pozo >= 5:
            print("\x1b[1;32m"+"*" * 50)
            print("\t", "\x1b[1;35m")
            apuesta_jugador = int(input("INGRESE SU APUESTA!! (monto multiplo de 5 y menor a su pozo actual): "))
            while apuesta_jugador % 5 != 0 or apuesta_jugador > pozo or apuesta_jugador == 0:
                apuesta_jugador = int(input("\x1b[1;33m"+"Monto invalido. Ingrese otro: "))
            acum_apuestas += apuesta_jugador
            contador_jugadas += 1

            print("\x1b[1;39m"+"POZO ACTUAL DEL JUGADOR","\x1b[1;31m", pozo)
            print("\x1b[1;39m"+"MONTO DE LA APUESTA: ", "\x1b[1;31m", apuesta_jugador)

            # random de cartas
            carta1_jugador = random.choice(numeros)
            carta1_jugador_palo = random.choice(palos)
            carta2_jugador = random.choice(numeros)
            carta2_jugador_palo = random.choice(palos)
            carta1_crupier = random.choice(numeros)
            carta1_crupier_palo = random.choice(palos)
            # PRUEBAS
           #carta1_jugador = AS
            # carta2_jugador = 10
            # carta1_crupier = AS

            if carta1_jugador == "AS" or carta2_jugador == "AS":
                salioUnAS = True
            if carta1_jugador == "AS" and carta2_jugador == "AS":
                salioDosAS = True
                salioUnAS = False
#******************** PRIMERA JUGADA ****************************************************************
            jugada_inicial()
            puntaje_jugador = puntaje_dos_cartas(carta1_jugador, carta2_jugador)
            puntaje_crupier = puntaje_una_carta(carta1_crupier)
            # ASIGNO EL VALOR DEL AS
            if carta1_crupier == "AS":
                puntaje_crupier += 11
                bandera_crup_AS = True
            # Mostramos el puntaje obtenido
            print("\x1b[1;39m"+"Puntaje obtenido por el jugador:","\x1b[1;31m", puntaje_jugador)
            print("\x1b[1;39m"+"Puntaje obtenido por el crupier:","\x1b[1;31m", puntaje_crupier)
             # BLACKJACK NATURAL
            if puntaje_jugador == 21:
                naturalJug = True
            selec = None
            cont  = 0
            band00 = bandAS = bandAS1 = bandAS2 = yapaso = descYaH = bandDes = band1 = False
#******************** SI EL PUNTAJE JUGADOR < 21 ****************************************************************
            while puntaje_jugador < 21:
                print("\x1b[1;39m")
                selec = int(input("Desea tirar otra carta?: (1: Si / 2: No): "))
                if selec == 1:
                    # lanza carta extra
                    carta_extra_num1 =  random.choice(numeros)
                    carta_extra_palo1 = random.choice(palos)
                    #carta_extra_num1 = AS
                    puntaje_jugador += puntaje_una_carta(carta_extra_num1)
                    if descYaH:
                        yapaso = False
                    # Si ya paso un AS antes y el punt es mayor a 21 vuelvo el AS a 1
                    if not bandAS2 and yapaso and puntaje_jugador > 21:
                        puntaje_jugador -= 10
                        descYaH = True
                    #BANDERAS
                    # prendo una bandera si sale AS
                    if carta_extra_num1 == "AS":
                        bandAS = True
                        yapaso = True # para la segunda ronda

                    if not salioUnAS and salioDosAS:
                        puntaje_jugador += puntaje_una_carta(carta_extra_num1)

                    # Para que me vuelva el AS que ya salio em la primer ronda a 1 si el punt es mayor a 21
                    if band1: # Para que el desc e lo haga una sola vez
                        salioUnAS = False
                    if not salioDosAS and salioUnAS:
                        if puntaje_jugador > 21:
                            puntaje_jugador -= 10
                            band1 = True
#************************************************************************************
                    # Si salieron dos AS antes
                    if bandAS and salioDosAS :
                        puntaje_jugador += 1
                        bandAS = False
#************************************************************************************
                    # Sale AS y salio 1 AS en las primeras cartas
                    # 2 vuelta viene otro AS
                    if bandAS and band00:
                        puntaje_jugador += 1
                        bandAS = False
                    # primer vuelta
                    if not bandDes and bandAS and salioUnAS: # agregue if  not bandDes
                        band00 = True
                        puntaje_jugador -= 9
#************************************************************************************
                    # cuando sale AS y antes NO salio AS
                    # 3 vuelta que viene AS
                    if bandAS and bandAS2:
                        puntaje_jugador += 1
                        bandAS = False
                    # 2 vuelta si viene otro AS
                    if bandAS and bandAS1:
                        puntaje_jugador -= 9
                        bandAS2 = True
                        bandAS = False
                        bandAS1 = False
                        if bandDes:
                            puntaje_jugador += 10
                    # 1 vuelta
                    if bandAS:
                        if carta1_jugador != "AS" and carta2_jugador != "AS":
                            puntaje_jugador += 11
                            bandAS1 = True
                            #Si al aparecer el primer AS el puntaje es mas alto de 21 lo vuelvo a 1
                            if puntaje_jugador > 21:
                                puntaje_jugador -= 10
                                bandDes = True
                    bandAS = False
#************************************************************************************
                    # Muestro resultados
                    print("\x1b[1;32m"+"Carta extra: ",
                        "\x1b[1;33m", carta_extra_num1, "de", "'" + carta_extra_palo1 + "'")
                    print("\x1b[1;39m"+"\nPuntaje obtenido por el JUGADOR","\x1b[1;31m", puntaje_jugador)
                if 1 > selec > 2:
                    selec = int(input("Opcion incorrecta...Desea tirar otra carta?: (1: Si / 2: No): "))
                if selec == 2:
                    break
            # reinicio de banderas
            salioDosAS = salioUnAS = bandera_crup_AS = False
            band00 = bandAS = bandAS1 = yapaso = descYaH = bandDes = band1 = False
            print("\x1b[1;39m"+"*" * 50)
            print("\x1b[1;31m"+" TURNO DEL CRUPIER")
#********************** MIENTRAS EL CRUPIER OBTENGA MENOS DE 17 PUNTOS **************************************************************
            band00 = bandAS = bandAS1 = bandAS2 = yapaso = descYaH = bandDes = band1 = False
            while puntaje_crupier < 17:
                cont += 1
                print("\x1b[1;39m"+"*" * 50)
                print("\x1b[1;31m"+"El crupier obtuvo : ","\x1b[1;31m", puntaje_crupier)
                print("\x1b[1;39m"+"Al ser menor a 17 puntos debe continuar tirando cartas...")
                carta_extra_num2 = random.choice(numeros)
                carta_extra_palo2 = random.choice(palos)
                # pruebas
                # carta_extra_num2 = AS
                puntaje_crupier += puntaje_una_carta(carta_extra_num2)
                if descYaH:
                    yapaso = False
                # Si ya paso un AS antes y el punt es mayor a 21 vuelvo el AS a 1
                if not bandAS2 and yapaso and puntaje_crupier > 21:
                    puntaje_crupier -= 10
                    descYaH = True
                #BANDERAS
                # prendo una bandera si sale AS
                if carta_extra_num2 == "AS":
                    bandAS = True
                    yapaso = True # para la segunda ronda



                # Para que me vuelva el AS que ya salio em la primer ronda a 1 si el punt es mayor a 21
                if band1: # Para que el desc e lo haga una sola vez
                    bandera_crup_AS = False
                if bandera_crup_AS:
                    if puntaje_crupier > 21:
                        puntaje_crupier -= 10
                        band1 = True

#************************************************************************************
                # Sale AS y salio 1 AS en las primeras cartas
                # 2 vuelta viene otro AS
                if bandAS and band00:
                    puntaje_crupier += 1
                    bandAS = False
                # primer vuelta
                if not bandDes and bandAS and bandera_crup_AS: # agregue if  not bandDes
                    band00 = True
                    puntaje_crupier -= 9
#************************************************************************************
                # cuando sale AS y antes NO salio AS
                # 3 vuelta que viene AS
                if bandAS and bandAS2:
                    puntaje_crupier += 1
                    bandAS = False
                # 2 vuelta si viene otro AS
                if bandAS and bandAS1:
                    puntaje_crupier -= 9
                    bandAS2 = True
                    bandAS = False
                    bandAS1 = False
                    if bandDes:
                        puntaje_crupier += 10
                # 1 vuelta
                if bandAS:
                    if carta1_crupier != "AS":
                        untaje_crupier += 11
                        bandAS1 = True
                #Si al aparecer el primer AS el puntaje es mas alto de 21 lo vuelvo a 1
                        if puntaje_crupier > 21:
                            puntaje_crupier -= 10
                            bandDes = True
                bandAS = False



                # BLACKJACK NATURAL
                if cont == 1 and puntaje_crupier == 21:
                    naturalCrup = True
#************************************************************************************
                    # Muestro resultados
                # Muestro resultados Crupier
                bandera = False
                print("\x1b[1;32m"+"Carta extra: ",
                 "\x1b[1;33m", carta_extra_num2, "de", "'" + carta_extra_palo2 + "'")
                print("\x1b[1;39m"+"\n Puntaje obtenido por el CRUPIER","\x1b[1;31m", puntaje_crupier)
            bandera = bandera1 = bandera2 = bandera3 = bandDes1 = unavez = yahicedes = bandera_crup = bandera_crup_AS = False
#************************************************************************************
            # Mostrar Ganadores
           # """ SI UNO DE LOS DOS SACAN BLACKJACK NATURAL"""
            if naturalCrup or naturalJug:
                 cm += 1
      #""" SI LOS DOS SACAN BLACKJACK NATURAL"""
            if naturalCrup and naturalJug:
                print("\x1b[1;32m"+">>> SE HA PRODUCIDO UN EMPATE <<<")
                print("\x1b[1;33m" + "El jugador: " + nombre_jugador, "RECIBE SU APUESTA")
                pozo += apuesta_jugador
                if apuesta_jugador > perd_mas_grande:
                    perd_mas_grande = apuesta_jugador
           # """  BLACKJACK NATURAL CRUPIER """
            if naturalCrup:
                print("\x1b[1;32m"+">>> BlackJack Natural del Crupier <<<")
                ganadorCrupier = True
            else: # Gana Jugador
                if not puntaje_jugador > 21:
                    if puntaje_jugador > puntaje_crupier or puntaje_crupier > 21 or naturalJug:
                        print("\x1b[1;32m"+">>> EL GANADOR ES EL", "\x1b[1;31m" + nombre_jugador + "\x1b[1;32m" + " <<<")
                        contador_gana_jugador += 1
                        ganadorJugador = True
                        print("\x1b[1;33m" + "El jugador: " + nombre_jugador, "DOBLA SU APUESTA")
                        pozo -= apuesta_jugador
                        pozo += (apuesta_jugador * 2)
                        if pozo > cont_may_pozo:
                            cont_may_pozo = pozo
            #"""  BLACKJACK NATURAL JUGADOR """
            if naturalJug:
                print("\x1b[1;32m"+">>> BlackJack Natural del Jugador ",  nombre_jugador, " <<<")
                ganadorJugador = True
            else:# gana crupier
                if not puntaje_crupier > 21:
                    if puntaje_crupier > puntaje_jugador or puntaje_jugador > 21 or naturalCrup:
                        print("\x1b[1;32m"+">>> EL GANADOR ES EL", "\x1b[1;31m" + "CRUPIER" + "\x1b[1;32m" + " <<<")
                        print("\x1b[1;33m"+ "El jugador: " + nombre_jugador, "PIERDE SU APUESTA")
                        pozo -= apuesta_jugador
                        if apuesta_jugador > perd_mas_grande:
                            perd_mas_grande = apuesta_jugador
                        ganadorCrupier = True
                        contador_gana_crupier += 1
          # EMPATE CON PUNTAJE MENOR A 21
            if not naturalCrup:
                if not naturalJug:
                    if puntaje_jugador <= 21 and puntaje_crupier <= 21:
                        if puntaje_crupier == puntaje_jugador:
                            print("\x1b[1;32m" + ">>> SE HA PRODUCIDO UN EMPATE <<<")
                            print("\x1b[1;33m" + "El jugador: " + nombre_jugador, "RECIBE  SU APUESTA")
            if puntaje_crupier > 21 and puntaje_jugador > 21:
                print(">>> AMBOS JUGADORES OBTUVIERON MAS DE 21 PUNTOS <<<")
                print("\x1b[1;32m"+">>> EL GANADOR ES EL", "\x1b[1;31m" + "CRUPIER" + "\x1b[1;32m" + " <<<")
                ganadorCrupier = True
                contador_gana_crupier += 1
                print("\x1b[1;33m" + "El jugador: " + nombre_jugador, "PIERDE SU APUESTA")
                pozo -= apuesta_jugador
                if apuesta_jugador > perd_mas_grande:
                    perd_mas_grande = apuesta_jugador
        print("\x1b[1;39m"+"POZO ACTUAL DEL JUGADOR", pozo)
        # 2) La racha más larga de victorias del croupier.
        if not naturalCrup:
            if ganadorCrupier:
                cont_gana_crupier += 1
                if cont_gana_crupier > mayor:
                    mayor = cont_gana_crupier
        if ganadorJugador:
            cont_gana_crupier = 0
        naturalJug = naturalCrup = ganadorCrupier = ganadorJugador = False
        menu()
        op = int(input("Opcion seleccionada: "))
    if op == 3:
        print("\x1b[1;39m" + "·"* 50)
        print("\x1b[1;39m" + "Cantidad de Jugadas totales: ", "\x1b[1;31m" , contador_jugadas)
        # 1) El porcentaje de victorias del jugador.
        if contador_jugadas == 0:
            porc_vic_jug = 0
        else:
            porc_vic_jug = contador_gana_jugador * 100 // contador_jugadas
        print("\x1b[1;39m" + "El porcentaje de victorias del jugador es de: ", "\x1b[1;31m" , porc_vic_jug, "%", "\x1b[1;39m", "en el total de jugadas")

        # 2) La racha más larga de victorias del croupier.
        print("\x1b[1;39m" + "La racha más larga de victorias del croupier es de: ", "\x1b[1;31m" , mayor, "\x1b[1;39m", "veces")

        # 3) La cantidad de manos donde hubo un blackjack natural
        print("\x1b[1;39m" + "Cantidad de manos donde hubo un blackjack natural: ", "\x1b[1;31m" , cm)

        # 4) El monto máximo que llegó a tener el jugador en el pozo.
        print("\x1b[1;39m" + "El monto máximo que llegó a tener el jugador en el pozo $", "\x1b[1;31m" , cont_may_pozo)


        # 5) El monto promedio del que dispuso el jugador para realizar apuestas.
        if contador_jugadas == 0:
            prom_apu = 0
        else:
            prom_apu = acum_apuestas // contador_jugadas
        print("\x1b[1;39m" + "El monto promedio del que dispuso el jugador para realizar apuestas: $ " , "\x1b[1;31m" ,prom_apu)

        # 6) La pérdida más grande que sufrió el jugador (si hubo alguna)
        print("\x1b[1;39m" + "La pérdida más grande que sufrió el jugador (si hubo alguna): $ ", "\x1b[1;31m" , perd_mas_grande)

        break

    if op > 3 or op <= 0:
        print("\x1b[1;39m")
        op = int(input("Opcion INCORRECTA: "))
        print("\x1b[1;32m" + "*" * 50)
print("\x1b[1;39m" +"Gracias por jugar")
