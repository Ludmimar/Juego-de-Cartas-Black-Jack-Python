"""Desarrolle un programa que permita generar una sucesión de mil números enteros aleatorios,
usando como semilla del generador al valor 11. Los números generados deben estar entre 1 y 2500
(ambos incluidos). A partir de esa sucesión, el programa debe informar:

Cuántos números eran divisibles por 4 pero no por 8, y cuántos eran divisibles por ambos
El promedio de los valores mayores a 2000
Cuántos números eran menores al primer valor generado y qué porcentaje representan
sobre el total de números
Si alguna vez aparecieron en la secuencia los valores extremos del intervalo (1, 2500)

import random
random.seed(11)
op = 1
div_por_cuatro = div_por_ocho = div_por_ambos = cont = suma = primer_valor = cont_menor = 0
bandera_uno = False


for i in range (1000):
    num = random.randint(1,2500)

    # Cuántos números eran menores al primer valor generado y qué porcentaje representan
    # sobre el total de números
    if i == 0:
        primer_valor = num
    if num < primer_valor:
        cont_menor += 1
    # El promedio de los valores mayores a 2000
    if num > 2000:
        cont += 1
        suma += num
    # Cuántos números eran divisibles por 4 pero no por 8, y cuántos eran divisibles por ambos
    if num % 4 == 0:
        if num % 8 != 0:
            div_por_cuatro += 1
        else:
            div_por_ambos += 1
    if num == 1 or num == 2500:
        bandera_uno = True


print("Numeros divisibles por 4 y no por 8: ", div_por_cuatro)
print("Numeros divisibles por 4 y 8: ", div_por_ambos)
if cont == 0:
    promedio = 0
else:
    promedio = suma / cont
print("El promedio de los valores mayores a 2000: ", round(promedio,2))

# Cuántos números eran menores al primer valor generado y qué porcentaje representan
# sobre el total de números
porcentaje = cont_menor * 100 / 1000
print ("Cantidad de números menores al primer valor generado: ", cont_menor)
print("Porcentaje que representan sobre el total: ", round(porcentaje,2), "%")
if bandera_uno == True:
    print("Aparecio el numero 1 o 2500 al menos una vez")
else:
    print("No aparecieron el numero 1 o 2500")
"""


"""2. Ejercicio con secuencia de números aleatorios
Generar una secuencia de n números aleatorios. El valor de n se ingresa por teclado, 
validar que sea mayor a 0.

Determinar:
a) Cuántos números terminan en 5. XXX
b) El porcentaje de números pares en la secuencia.
c) Cual es el menor número múltiplo de 3 de la secuencia.
d) La cantidad de veces que aparece el primer número de la secuencia."""

import random
random.seed(11)

cant_pares = primer_num = cont_primer_valor = nm3 = 0

n = 0
while n <= 0:
 n = int(input('Ingrese la cantidad de numeros a procesar: '))
 if n <= 0:
     print('Error!!! El numero debe ser mayor a cero')
for i in range(n):
    num = random.randint(1, 1000)
    print(num)
    if i == 0:
        primer_num = num

    if num % 2 == 0:
        cant_pares +=1
    if num == primer_num:
        cont_primer_valor += 1
    if num % 3 == 0:
        nm3 = num


print("·"*50)
# b) El porcentaje de números pares en la secuencia.
porc_pares = cant_pares * 100 / n
print("El porcentaje de números pares en la secuencia es: ", round(porc_pares, 2), "%")
# La cantidad de veces que aparece el primer número de la secuencia.
print("La cantidad de veces que aparece el primer número de la secuencia es : ", cont_primer_valor)
















"""
while op != 4:
    print('*' * 50)
    print("MENU DE OPCIONES")
    print('*' * 50)
    print("OPCION 1")
    print("OPCION 2")
    print("OPCION 3")
    print("Salir)")

    op = int(input("Ingrese la opcion seleccionada: "))
    if op == 1:
        print("OPCION 1")
    elif op == 2:
        print("OPCION 2")
    elif op == 3:
        print("OPCION 3")
    elif op == 4:
        print("Adios!")
    elif op > 4:
        print("Selecciono una opcion incorrecta!")
"""
