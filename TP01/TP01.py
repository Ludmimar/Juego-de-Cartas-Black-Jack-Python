import random
AS = "AS"
J = "J"
Q = "Q"
K = "K"
numeros = (AS, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
palos = "Corazones", "Diamantes", "Pica", "Treboles"
puntaje_crupier = puntaje_jugador = 0
carta1 = random.choice(numeros)
carta1_palo = random.choice(palos)
carta2 = random.choice(numeros)
carta2_palo = random.choice(palos)
print("\x1b[1;31m"+"\t\t***** BLACK JACK *****")
print("\x1b[1;39m"+"Reglas: El jugador que obtenga el mayor puntaje\n"
      "cercano al 21 (sin pasarse) GANA!")
print("El AS vale 11 puntos siempre y cuando el puntaje\n"
      "final no sea mayor a 21 (si es mayor a 21 el AS\n"
      "pasa a valer 1 punto). Si sacas mas de un AS, cada \n"
      "uno vale 1 punto. Las figuras valen 10 puntos.")
print("\x1b[1;32m"+"*" * 50)
print("\t", "\x1b[1;35m"+"**** JUGADA DEL CRUPIER ****\n")
print("Las primeras dos cartas que salieron son:"
      "\x1b[1;33m"+"\n", carta1, "de", "'" + carta1_palo + "'", "y", carta2, "de", "'" + carta2_palo + "'")
if carta1 == "AS" and carta2 != "AS" or carta2 == "AS" and carta1 != "AS":
     puntaje_crupier += 11
elif carta1 == AS and carta2 == AS:
    puntaje_crupier += 2
if carta1 != "AS" and carta1 != "J" and carta1 != "Q" and carta1 != "K":
    puntaje_crupier += carta1
if carta2 != "AS" and carta2 != "J" and carta2 != "Q" and carta2 != "K":
    puntaje_crupier += carta2
if carta1 == "J" or carta1 == "Q" or carta1 == "K":
    puntaje_crupier += 10
if carta2 == "J" or carta2 == "Q" or carta2 == "K":
    puntaje_crupier += 10
print("\x1b[1;35m"+"Puntaje obtenido:", puntaje_crupier)
carta3 = 0
carta3_palo = ""
if puntaje_crupier <= 16:
    carta3 = random.choice(numeros)
    carta3_palo = random.choice(palos)
    if carta1 == AS and carta2 == AS and carta3 == AS:
        puntaje_crupier += 1
    if carta3 != "AS" and carta3 != "J" and carta3 != "Q" and carta3 != "K":
        puntaje_crupier += carta3
    if carta3 == "J" or carta3 == "Q" or carta3 == "K":
        puntaje_crupier += 10
    if carta3 == "AS" and carta2 != "AS" and carta1 != "AS":
        puntaje_crupier += 11
        if puntaje_crupier > 21:
            puntaje_crupier -= 10
    if carta3 == "AS" and carta1 == "AS" and carta2 != "AS" or carta3 == "AS" and carta2 == "AS" and carta1 != "AS":
        puntaje_crupier -= 9
    if carta1 == "AS" or carta2 == "AS":
        if puntaje_crupier > 21:
            puntaje_crupier -= 10
    print("\x1b[1;32m"+"Obtuvo un puntaje menor a 17, se saca otra carta:")
    print("\x1b[1;35m"+"La tercer carta es:", "\x1b[1;33m", carta3, "de", "'" + carta3_palo + "'" )
print("\x1b[1;31m"+"Puntaje Final:", puntaje_crupier)
print("\x1b[1;32m"+"*" * 50)
print("\t", "\x1b[1;35m"+"**** JUGADA DEL JUGADOR ****\n")
carta12 = random.choice(numeros)
carta12_palo = random.choice(palos)
carta22 = random.choice(numeros)
carta22_palo = random.choice(palos)
print("Las primeras dos cartas que salieron son:"
      "\x1b[1;33m"+"\n", carta12, "de", "'" + carta12_palo + "'", "y", carta22, "de", "'" + carta22_palo + "'")
if carta12 == "AS" and carta22 != "AS" or carta22 == "AS" and carta12 != "AS":
    puntaje_jugador += 11
elif carta12 == AS and carta22 == AS:
    puntaje_jugador += 2
if carta12 != "AS" and carta12 != "J" and carta12 != "Q" and carta12 != "K":
    puntaje_jugador += carta12
if carta22 != "AS" and carta22 != "J" and carta22 != "Q" and carta22 != "K":
    puntaje_jugador += carta22
if carta12 == "J" or carta12 == "Q" or carta12 == "K":
    puntaje_jugador += 10
if carta22 == "J" or carta22 == "Q" or carta22 == "K":
    puntaje_jugador += 10
    figura = True
print("\x1b[1;35m"+"Puntaje obtenido:", puntaje_jugador)
carta32 = 0
carta32_palo = ""
if puntaje_jugador <= 16:
    carta32 = random.choice(numeros)
    carta32_palo = random.choice(palos)
    if carta12 == AS and carta22 == AS and carta32 == AS:
        puntaje_jugador += 1
    if carta32 != "AS" and carta32 != "J" and carta32 != "Q" and carta32 != "K":
        puntaje_jugador += carta32
    if carta32 == "J" or carta32 == "Q" or carta32 == "K":
        puntaje_jugador += 10
    if carta32 == "AS" and carta22 != "AS" and carta12 != "AS":
        puntaje_jugador += 11
        if puntaje_jugador > 21:
            puntaje_jugador -= 10
    if carta32 == "AS" and carta12 == "AS" and carta22 != "AS" or  carta32 == "AS" and carta22 == "AS" and carta12 != "AS":
        puntaje_jugador -= 9
    if carta12 == "AS" or carta22 == "AS":
        if puntaje_jugador > 21:
            puntaje_jugador -= 10
    print("\x1b[1;32m"+"Obtuvo un puntaje menor a 17, se saca otra carta:")
    print("\x1b[1;35m"+"La tercer carta es:","\x1b[1;33m", carta32, "de", "'" + carta32_palo + "'" )
print("\x1b[1;31m"+"Puntaje Final:", puntaje_jugador)
print("\x1b[1;32m"+"*" * 50)
if not puntaje_crupier > 21:
    if puntaje_crupier > puntaje_jugador or puntaje_jugador > 21:
        print("\x1b[1;32m"+">>> EL GANADOR ES EL", "\x1b[1;31m" + "CRUPIER" + "\x1b[1;32m" + " <<<")
if not puntaje_jugador > 21:
    if puntaje_jugador > puntaje_crupier or puntaje_crupier > 21:
        print("\x1b[1;32m"+">>> EL GANADOR ES EL", "\x1b[1;31m" + "JUGADOR " + "\x1b[1;32m" + " <<<")
if puntaje_jugador == puntaje_crupier and puntaje_crupier <= 21 and puntaje_jugador <= 21:
    print("\x1b[1;32m"+">>> SE HA PRODUCIDO UN ", "\x1b[1;31m" + "EMPATE " + "\x1b[1;32m" + " <<<")
if puntaje_crupier > 21 and puntaje_jugador > 21:
    print("\x1b[1;32m"+">>> AMBOS JUGADORES ", "\x1b[1;31m" + "PERDIERON " + "\x1b[1;32m" + " <<<")
if carta1_palo == carta12_palo:
    print("\x1b[1;32m"+" * Ambos jugadores obtuvieron *", "\n", "* EL MISMO PALO EN SU PRIMER CARTA * ")
    if carta1 == carta12:
        print("\x1b[1;32m"+"** Ademas COINCIDEN EN EL NUMERO O FIGURA **")
if carta1 == "J" or carta1 == "Q" or carta1 == "K" or carta2 == "J" or carta2 == "Q" or carta2 == "K" or\
 carta3 == "J" or carta3 == "Q" or carta3 == "K" or carta12 == "J" or carta12 == "Q" or carta12 == "K" or \
 carta22 == "J" or carta22 == "Q" or carta22 == "K" or carta32 == "J" or carta32 == "Q" or carta32 == "K":
    print("\x1b[3;32m"+"\n --- Salio al menos una FIGURA --- ")
