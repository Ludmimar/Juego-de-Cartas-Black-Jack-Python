"""
print("Guía de Ejercicios Prácticos - Ficha 04")
print('*' * 30)
print('01) Generador de Mails')

print('\nIngreso de datos:')
nombre = input('\tNombre : ')
apellido = input('\tApellido: ')
dominio = input('\tDominio : ')

#transformar las cadenas ingresadas en minúscula
# independientemente de cómo se ingresaron.
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()
primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_apellido != primera_letra_nombre:
    mail_propuesto = primera_letra_nombre + apellido + '@' + dominio
else:
    mail_propuesto = nombre + '.' + apellido + '@' + dominio

print()
print('Mail propuesto:\n\t', mail_propuesto)


print("*" * 50)
print('2) Suma - División - Potencia')
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))
suma = a + b + c
if suma > 10:
    result = suma // 2
else:
    result = suma ** 3

print("Resultado: ", result)

print("*" * 50)
print('3) Jornal de un Operario')

turno = int(input("Ingrese el codigo de turno (1- representa Diurno y 2- representa Nocturno):" ))
horas = int(input("Cantidad de horas trabajadas: "))

if turno == 1:
    sueldo = horas * 35.50
else:
    sueldo = horas * 40.60

print("El sueldo es de: $", sueldo)


print("*" * 50)
print('3) Jornal de un Operario')
"""
print(10 % 4)
