import random
from Soporte import *

AS = "AS"
J = "J"
Q = "Q"
K = "K"
numeros = (AS, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
palos = "Corazones", "Diamantes", "Pica", "Treboles"
puntaje_crupier = puntaje_jugador = 0
# Generamos las cartas automaticamente
carta1_jugador = random.choice(numeros)
carta1_jugador_palo = random.choice(palos)
carta2_jugador = random.choice(numeros)
carta2_jugador_palo = random.choice(palos)
carta1_crupier = random.choice(numeros)
carta1_crupier_palo = random.choice(palos)

#carta1_crupier = AS
#carta1_jugador = AS
# carta2_jugador = AS

import random


AS = "AS"
J = "J"
Q = "Q"
K = "K"
numeros = (AS, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
palos = "Corazones", "Diamantes", "Pica", "Treboles"
puntaje_crupier = puntaje_jugador = 0
# Generamos las cartas automaticamente

def menu():
    print("*"*50)
    print("Seleccione su jugada:")
    print("1: Apostar")
    print("2: Jugar una Mano")
    print("3: Salir")

def jugada_inicial():
    print("Cartas del Jugador: ")
    print("Primer carta: ", carta1_jugador, "de", carta1_jugador_palo)
    print("Primer carta: ", carta2_jugador, "de", carta2_jugador_palo)
    print("Carta del Crupier: ")
    print("Primer carta: ", carta1_crupier, "de", carta1_crupier_palo)

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

print("*** BIENVENIDO AL JUEGO DEL BLACKJACK 2.0 ***")
pozo = 0
naturalJug = naturalCrup = False
salioUnAS = salioDosAS = bandera_crup_AS = False
contador_jugadas = 0
contador_gana_jugador = contador_gana_crupier = porc_vic_jug = 0
# solicitamos nombre del jugador
maximo = 100000
nombre_jugador = input("Ingrese su nombre: ")
ganadorJugador = ganadorCrupier =  False

# monto del pozo
pozo = int(input("Ingrese el monto del pozo inicial (mayor a 0 y menor a 100000): "))
while pozo <= 0 or pozo > maximo:
    pozo = int(input("Error!!! Ingrese el monto del pozo inicial (mayor a 0 y menor a 100000):"))
menu()
op = int(input("Opcion seleccionada: "))
while op != 4:
    if op == 1: #  QUEDO OK
        # esta opcion es para agregar plata al pozo que no supere maximo

        monto = int(input("Ingrese el monto a sumar al pozo: "))
        pozo += apostar(monto)
        print("POZO ACTUAL DEL JUGADOR", pozo)
        menu()
        op = int(input("Opcion seleccionada: "))

    if op == 2:
        if pozo < 5:
            opc = int(input("Su pozo es muy bajo...desea ingresar mas dinero? (1 = si, 2 = no ): "))
            if opc == 1:
                monto = int(input("Ingrese el monto a sumar al pozo: "))
                pozo += apostar(monto)


        if pozo >= 5:
            apuesta_jugador = int(input("Monto de la apuesta (multiplo de 5) y menor a su pozo actual: "))
            while apuesta_jugador % 5 != 0 or apuesta_jugador > pozo or apuesta_jugador == 0:
                apuesta_jugador = int(input("Monto invalido. Ingrese otro: "))
            contador_jugadas += 1
            # RESTO DEL POZO LA APUESTA
            print("MONTO DE LA APUESTA: ", apuesta_jugador)
            pozo -= apuesta_jugador
            print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ")
            print("Su apuesta se desconto del pozo hasta obtener el resultado de la partida")
            print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ")
            print("POZO ACTUAL DEL JUGADOR", pozo)
            # random de cartas
            carta1_jugador = random.choice(numeros)
            carta1_jugador_palo = random.choice(palos)
            carta2_jugador = random.choice(numeros)
            carta2_jugador_palo = random.choice(palos)
            carta1_crupier = random.choice(numeros)
            carta1_crupier_palo = random.choice(palos)
            # PRUEBAS
            carta1_jugador =AS
            # carta2_jugador = 10
            carta1_crupier = 1

            if carta1_jugador == "AS" or carta2_jugador == "AS":
                salioUnAS = True
            if carta1_jugador == "AS" and carta2_jugador == "AS":
                salioDosAS = True
                salioUnAS = False
#******************** PRIMERA JUGADA ****************************************************************
            jugada_inicial()
            puntaje_jugador = puntaje_dos_cartas(carta1_jugador, carta2_jugador)
            puntaje_crupier = puntaje_una_carta(carta1_crupier)

            if carta1_crupier == AS:
                puntaje_crupier += 11
                bandera_crup_AS = True

            # Mostramos el puntaje obtenido
            print("Puntaje obtenido por el jugador:", puntaje_jugador)
            print("Puntaje obtenido por el crupier:", puntaje_crupier)
            # Pregunto si con las dos primeras cartas alcanzo blackjack natural
            if puntaje_jugador == 21:
                naturalJug = True
            selec = None
            cont  = 0
            band00 =  False
            bandAS = bandAS1 = bandAS2 = yapaso = descYaH = False
            bandDes = band1 = False

            cv = 0
#******************** SI EL PUNTAJE JUGADOR < 21 ****************************************************************
            while puntaje_jugador < 21:
                selec = int(input("Desea tirar otra carta?: (1: Si / 2: No): "))
                if selec == 1:
                    # lanza carta extra
                    carta_extra_num1 =  random.choice(numeros)
                    carta_extra_palo1 = random.choice(palos)
                    # carta_extra_num1 = 5

                #BANDERAS
                # prendo una bandera si sale AS
                if carta_extra_num1 == AS:
                    bandAS = True
                    yapaso = True # para la segunda ronda

                """while bandAS:
                    cv += 1
                    if cv == 1:
                        # SI YA SALIERON DOS AS ANTES
                        if salioDosAS:
                            puntaje_jugador += 1
                        # SI SALIO UN AS ANTES 
                        elif salioUnAS:
                            puntaje_jugador -= 9
                            band00 = True #PRENDO UNA BANDERA"""




#************************************************************************************
                if not descYaH:
                        puntaje_jugador += puntaje_una_carta(carta_extra_num1)
                    # Si ya paso un AS antes y el punt es mayor a 21 vuelvo el AS a 1
                if not bandDes and yapaso and puntaje_jugador > 21:
                        puntaje_jugador -= 10
                        descYaH = True
                    #BANDERAS
                    # prendo una bandera si sale AS
                    if carta_extra_num1 == AS:
                        bandAS = True
                        yapaso = True # para la segunda ronda

                    # Si salieron dos AS antes
                    if bandAS and salioDosAS :
                        puntaje_jugador += 1
#************************************************************************************
                    # Sale AS y salio 1 AS en las primeras cartas
                    # 2 vuelta viene otro AS
                    if bandAS and band00:
                        puntaje_jugador += 1
                        bandAS = band00 = False
                    # primer vuelta
                    if not bandDes and bandAS and salioUnAS: # agregue if  not bandDes
                        band00 = True
                        puntaje_jugador -= 9
#************************************************************************************
                    # cuando en las primeras cartas NO salio AS
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
                    # si la carta extra es un AS (y antes no salio) que sume 11 punto
                    if bandAS:
                        if carta1_jugador != AS and carta2_jugador != AS:
                            puntaje_jugador += 11
                            bandAS1 = True
                            #Si al aparecer el primer AS el puntaje es mas alto de 21 lo vuelvo a 1
                            if puntaje_jugador > 21:
                                puntaje_jugador -= 10
                                bandDes = True
#************************************************************************************
                    # Para que me vuelva el AS que ya salio a 1 si el punt es mayor a 21
                    if band1: # Para que el desc e lo haga una sola vez
                        salioUnAS = False

                    if salioUnAS:
                        if puntaje_jugador > 21:
                            puntaje_jugador -= 10
                            band1 = True
#************************************************************************************
                    # Muestro resultados
                    print("Carta extra: ", carta_extra_num1, "de", carta_extra_palo1)
                    print("Puntaje obtenido por el JUGADOR", puntaje_jugador)


                if 1 > selec > 2:
                    selec = int(input("Opcion incorrecta...Desea tirar otra carta?: (1: Si / 2: No): "))
                if selec == 2:
                    break
                bandAS =  False
#********************** MIENTRAS EL CRUPIER OBTENGA MENOS DE 17 PUNTOS **************************************************************
            bandera = bandera1 = bandera2 = bandera3 = bandDes = unavez = yahicedes = False
            while puntaje_crupier < 17:
                cont += 1
                print("*"*50)
                print("El crupier obtuvo : ", puntaje_crupier)
                print("Al ser menor a 17 puntos debe continuar tirando cartas...")
                carta_extra_num2 = random.choice(numeros)
                carta_extra_palo2 = random.choice(palos)
                # pruebas
                # carta_extra_num2 = 10
                if not yahicedes:
                    puntaje_crupier += puntaje_una_carta(carta_extra_num2)
                if not bandDes and unavez and puntaje_crupier > 21:
                    puntaje_crupier -= 10
                    yahicedes = True
                if carta_extra_num2 ==  AS:
                    bandera = True
                    unavez = True
#************************************************************************************
                #SI SALE AS Y ANTES YA SALIO
                # vuelta 2 en adelante
                if bandera and bandera1:
                    puntaje_crupier += 1
                    bandera = bandera1 = False
                    # vuelta 1
                    # Si antes salio AS y ahora sale AS que cada uno valga 1 punto
                if not bandDes and bandera and bandera_crup_AS:
                    puntaje_crupier -= 9
                    bandera1 = True


#************************************************************************************
                #SI SALE AS Y ANTES NO SALIO
                # 3 vuelta
                if bandera and bandera3:
                    puntaje_crupier += 1
                    bandera = False
                # 2 vuelta
                if bandera and bandera2:
                    puntaje_crupier -= 9
                    bandera = bandera2 = False
                    bandera3 = True
                    if bandDes:
                        puntaje_jugador += 10
                # 1 vuelta
                if bandera and carta1_crupier != AS:
                    puntaje_crupier += 11
                    bandera2 = True
                    bandera = False #Agregue
                    if puntaje_crupier > 21:
                        puntaje_crupier -= 10
                        bandDes = True
#************************************************************************************

                if cont == 1 and puntaje_crupier == 21:
                    naturalCrup = True
                if bandera_crup_AS:
                    bandera = False
                if bandera and puntaje_jugador > 21:
                    puntaje_jugador -= 10
                    bandera_crup_AS = True
                bandera = False
                # Muestro resultados Crupier
                print("Carta extra: ", carta_extra_num2, "de", carta_extra_palo2)
                print("Puntaje obtenido por CRUPIER: ", puntaje_crupier)
#************************************************************************************
            # Mostrar Ganadores
             # EMPATE CON BLACKJACK NATURAL
            if naturalCrup and naturalJug:
                print(">>> SE HA PRODUCIDO UN EMPATE <<<")
                pozo += apuesta_jugador
                print(nombre_jugador, "RECIBE SU APUESTA")
            # BlackJack natural Crupier
            if naturalCrup:
                    print(">>> BlackJack Natural del Crupier <<<")
                    contador_gana_crupier += 1
                    ganadorCrupier = True
            # Si no gana jugador
            else: # Gana Jugador
                if not puntaje_jugador > 21:
                    if puntaje_jugador > puntaje_crupier or puntaje_crupier > 21 or naturalJug:
                        print("Gana el jugador: ", nombre_jugador )
                        contador_gana_jugador += 1
                        ganadorJugador = True
                        pozo += apuesta_jugador * 2
                        print(nombre_jugador, "DOBLA SU APUESTA")
            # Determinar quién ha obtenido el mayor puntaje, el jugador o el croupier. Considerar que pueden empatar.
            # if not lo agrego para q si ambos jugadores sacan mas de 21 no ganen ambos
            if naturalJug:
                print(">>> BlackJack Natural del Jugador ",  nombre_jugador, " <<<")
                contador_gana_jugador += 1
                ganadorJugador = True
            else:
                if not puntaje_crupier > 21:
                    if puntaje_crupier > puntaje_jugador or puntaje_jugador > 21 or naturalCrup:
                        print("Gana el Crupier" )
                        print(nombre_jugador, "PIERDE SU APUESTA")
                        ganadorCrupier = True
                        contador_gana_crupier += 1
            # EMPATE CON PUNTAJE MENOR A 21
            if puntaje_jugador <= 21 and puntaje_crupier <= 21:
                if puntaje_crupier == puntaje_jugador:
                    print(">>> SE HA PRODUCIDO UN EMPATE <<<")
                    print(nombre_jugador, "RECIBE  SU APUESTA")
                    pozo += apuesta_jugador
            if puntaje_crupier > 21 and puntaje_jugador > 21:
                print(">>> AMBOS JUGADORES OBTUVIERON MAS DE 21 PUNTOS <<<")
                print("Gana el crupier")
                ganadorCrupier = True
                contador_gana_crupier += 1
                print(nombre_jugador, "PIERDE SU APUESTA")

            print("POZO ACTUAL DEL JUGADOR: ", pozo)
            print("·"* 50)
            print("Cantidad de Jugadas Totales: ",  contador_jugadas)
            print("Jugador gano: ",contador_gana_jugador )
            print("Crupier gano: ",contador_gana_crupier )
            porc_vic_jug = contador_gana_jugador * 100 // contador_jugadas
            print("El porcentaje de victorias del jugador es de: ", porc_vic_jug, "%")

        naturalJug = naturalCrup =  False

        menu()
        op = int(input("Opcion seleccionada: "))

    if op == 3:
        # 1) El porcentaje de victorias del jugador.
        if contador_jugadas == 0:
            porc_vic_jug = 0
        else:
            porc_vic_jug = contador_gana_jugador * 100 // contador_jugadas
        print("El porcentaje de victorias del jugador es de: ", porc_vic_jug, "%")
        break

        # 2) La racha más larga de victorias del croupier.
        # 3) La cantidad de manos donde hubo un blackjack natural
        # 4) El monto máximo que llegó a tener el jugador en el pozo.
        # 5) El monto promedio del que dispuso el jugador para realizar apuestas.
        # 6) La pérdida más grande que sufrió el jugador (si hubo alguna)

    if op > 4 or op <= 0:
        op = int(input("Opcion INCORRECTA: "))


print("Gracias por jugar")
