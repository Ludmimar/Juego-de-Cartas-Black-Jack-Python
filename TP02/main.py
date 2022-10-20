                    if not descYaH:
                        if not salioDosAS:
                            puntaje_jugador += puntaje_una_carta(carta_extra_num1)
                    # Si ya paso un AS antes y el punt es mayor a 21 vuelvo el AS a 1
                    if not bandDes and yapaso and puntaje_jugador > 21:
                        puntaje_jugador -= 10
                        descYaH = True
                    if carta_extra_num1 == AS:
                        bandAS = True
                        yapaso = True # para la segunda ronda

                    # Si salieron dos AS antes
                    if bandAS and salioDosAS :
                        puntaje_jugador += 1
                        bandAS = False
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
