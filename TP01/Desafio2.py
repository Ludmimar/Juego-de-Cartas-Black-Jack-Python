print("Desafío 02 [Problema: La Sucesión 3n + 1 (o Sucesión de Collatz)]")

def collatz(num):
    sec = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        sec.append(num)
    return sec
suma = 0
n = int(input("Ingrese el numero de la secuencia: "))
secuencia = collatz(n)
print("Secuencia obtenida: ",secuencia)
for i in secuencia:
    # print(i, end=" ")
    suma += i
max = max(secuencia)
print("El numero maximo de la secuencia es: ", max)
long = len(secuencia)
print("La secuencia contiene : ", long, "numeros")
prom = suma / long
print("Promedio de los numeros de la secuencia: ", round(prom, 2))
# ********************************
print('*' * 50)
# PARA DEMOSTRAR QUE SE CUMPLE PARA TODOS LOS NUMEROS
def collatz(num):
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    if num == 1:
        return True
    else:
        return False

for i in range(1, 1_000_000):
    if i % 100_000 == 0:
        print("Comprobado hasta el :", i)
    if not collatz(i):
        print("No se cumple para el : ", i)
        break
else:
    print("Se cumple para todos los numeros")



