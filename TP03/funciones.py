import random
class Proyecto:
    def __init__(self,num_proy, titulo, fecha_d, fecha_m, fecha_a, tipo_leng, cant_lineas):
         self.num_proy = num_proy
         self.titulo = titulo
         self.fecha_d = fecha_d
         self.fecha_m = fecha_m
         self.fecha_a = fecha_a
         self.tipo_leng = tipo_leng
         self.cant_lineas =cant_lineas

def menu():
    print()
    print("\x1b[1;32m"+'▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ ▊ ▋ █ ▌'+' MENU DE OPCIONES '+ '▌ █ ▋ ▊ ▉ ▇ ▆ ▅ ▄ ▃ ▂ ▁ ')
    print(  '\n \t \t \t \t 1) ▶ Cargar Proyectos: '
            '\n \t \t \t \t 2) ▶ Listar Proyectos: '
            '\n \t \t \t \t 3) ▶ Actualizar Proyecto: '
            '\n \t \t \t \t 4) ▶ Resumen por lenguaje: '
            '\n \t \t \t \t 5) ▶ Resumen por año: '
            '\n \t \t \t \t 6) ▶ Filtrar por lenguaje: '
            '\n \t \t \t \t 7) ▶ Productividad: '
            '\n \t \t \t \t 8) ▶ Salir ')
    op = int(input("\x1b[1;33m"+' \t \t \t \t ➤ Ingrese una opcion: '))
    while op <= 0 or op > 8:
            op = int(input("\x1b[1;33m"+" \t \t \t \t ➤ Debe ingresar 1 opcion correcta: "))
    return op

def validar_n(n, min, max = False ):
    if max == False:
        while n <= min:
            n = int(input("\x1b[1;33m"+"\n \t \t \t \t ➤ Ingrese un número correcto: "))
    else:
        while n <= min or n > max:
            n = int(input("\x1b[1;33m"+"\n \t \t \t \t ➤ Ingrese un número correcto: "))
    return n

def crear_vector(v,c1):
    titulos = ('proyectoA', 'proyectoB', 'proyectoC', 'proyectoD', 'proyectoE')
    if c1==0:
        n = int(input("\n \t \t \t \t ➤ Cantidada de proyectos que desea cargar: "))
        v = v * n
        for i in range(len(v)):
            num_proy = i+1
            titulo = random.choice(titulos)
            fecha_d,fecha_m, fecha_a = str(random.randint(1,31)), str(random.randint(1,12)), str(random.randint(2000,2022))
            tipo_leng = random.randint(0, 10)
            cant_lineas = random.randint(100, 500)
            v[i] = (Proyecto(num_proy, titulo, fecha_d, fecha_m, fecha_a, tipo_leng, cant_lineas))
        print("\x1b[1;33m"+"\n \t \t \t \t 》》》》》》Proyectos Creados ✔ 《《《《《《")
    else:
        n = int(input("\n \t \t \t \t ➤ Cantidada de proyectos que desea agregar: "))
        pos = len(v)
        for i in range(n):
            v.append(pos + i + 1)
            num_proy = pos + i + 1
            titulo = random.choice(titulos)
            fecha_d,fecha_m, fecha_a = str(random.randint(1,31)), str(random.randint(1,12)), str(random.randint(2000,2022))
            tipo_leng = random.randint(0, 10)
            cant_lineas = random.randint(100, 500)
            v[pos+i] = (Proyecto(num_proy, titulo, fecha_d, fecha_m, fecha_a, tipo_leng, cant_lineas))
        print("\x1b[1;33m"+"\n \t \t \t \t 》》》》》》 Proyectos Agregados ✔ 《《《《《《")
    return v

def seleccion_directa(v):
    n = len(v)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if v[i].titulo > v[j].titulo:
                v[i], v[j] = v[j], v[i]

def write_punto_2(v):
    print()
    lenguajes = 'Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift',  'C#', 'VB', 'Go'
    for i in range(len(v)):
        n_lenguaje_actual = v[i].tipo_leng
        print("\x1b[1;39m" + f'～Número de proyecto: {v[i].num_proy}', end='～ ')
        print(f'Titulo: {v[i].titulo}', end='～ ')
        print(f'Fecha de actualización: {v[i].fecha_d} / {v[i].fecha_m} / {v[i].fecha_a} ', end='～ ')
        print(f'Lenguaje: {lenguajes[n_lenguaje_actual]}', end='～ ')
        print(f'Cantidad de lineas de código: {v[i].cant_lineas}～')

def punto_3(v):
    fecha_d = fecha_m = fecha_a = 0
    x = int(input('\t \t \t \t ➤ Ingrese el número de proyecto a buscar: '))
    i = busqueda_secuencial(v,x)
    if i != -1:
        v[i].fecha_d = int(input('\t \t \t \t ➤ Ingrese el dia:'))
        while v[i].fecha_d <= 0 or v[i].fecha_d >= 31:
            v[i].fecha_d = int(input('\t \t \t \t ➤ Ingrese el dia CORRECTAMENTE:'))

        v[i].fecha_m = int(input('\t \t \t \t ➤ Ingrese el mes:'))
        while v[i].fecha_m <= 0 or v[i].fecha_m >= 12:
            v[i].fecha_m = int(input('\t \t \t \t ➤ Ingrese el mes CORRECTAMENTE:'))

        v[i].fecha_a = int(input('\t \t \t \t ➤ Ingrese el año:'))
        while v[i].fecha_a <= 2000 or v[i].fecha_a >= 2022:
            v[i].fecha_a = int(input('\t \t \t \t ➤ Ingrese el año CORRECTAMENTE:'))

        v[i].cant_lineas = int(input('\t \t \t \t ➤ Ingrese la cantidad de lineas de código:'))
        print('\t \t \t \t 》Arreglo modificado correctamente ✔《')
    else:
        print('\t \t \t \t 》No existe un proyecto con ese número《')

def busqueda_secuencial(v, x):
    for i in range(len(v)):
        if x == v[i].num_proy:
            return i
    return -1

def punto_4(v):
    print()
    acu = acumuladores(v)
    for i in range(11):
        lenguajes = 'Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift',  'C#', 'VB', 'Go'
        print("\x1b[1;39m" + f'\t \t \t \t ❏ El lenguaje {lenguajes[i]} tuvo un total de: {acu[i]} lineas de código ❏')

def acumuladores(v):
    acumuladores = [0] * 11
    for i in range(len(v)):
        #n = v[i].cant_lineas
        pos = v[i].tipo_leng
        acumuladores[pos] += v[i].cant_lineas
    return acumuladores

def punto_5(v):
    print()
    contadores = fun_contadores(v)
    print("\x1b[1;39m" + "\t \t \t \t～ CANTIDAD TOTAL DE PROYECTOS POR AÑO ～")
    for i in range(len(contadores)):
        if contadores[i] > 0:
            print("\x1b[1;39m" + f'\t \t \t \t ▢ {2000 + i} ⫸ {contadores[i]}')
    return contadores

def fun_contadores(v):
    conta = [0] * 23
    for i in range(len(v)):
        n = int(v[i].fecha_a)
        pos = n - 2000
        conta[pos] += 1
    return conta

def punto_6(v):
    print()
    n = int(input("\x1b[1;33m" + '\t \t \t \t ➤ Ingrese el numero el cod. del lenguaje para filtrar: '))
    print()
    band1 = False
    n = validar_n(n, -1, 10)
    seleccion_directa_p6(v)
    for i in range(len(v)):
        if v[i].tipo_leng == n:
            band1 = True
            print("\x1b[1;39m" + f'～Número de proyecto: {v[i].num_proy}', end='～ ')
            print(f'Titulo: {v[i].titulo}', end='～ ')
            print(f'Fecha de actualización: {v[i].fecha_d} / {v[i].fecha_m} / {v[i].fecha_a} ', end='～ ')
            print(f'Lenguaje: {v[i].tipo_leng}', end='～')
            print(f'Cantidad de lineas de código: {v[i].cant_lineas}～')
    if not band1:
        print("\x1b[1;39m" + ' \t \t \t \t No se encontraron coincidencias')

def seleccion_directa_p6(v):
    n = len(v)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if v[i].num_proy > v[j].num_proy:
                v[i], v[j] = v[j], v[i]

def punto_7(con, v):
    print()
    may = 0
    mayores = []
    for i in range(len(con)):
        if con[i] > may:
            may = con[i]
    for j in range(len(con)):
        if con[j] == may:
            f = 2000 + j
            mayores.append(f)
    if len(mayores) > 1:
        print("\x1b[1;39m" + f"\t \t ～ Los años con mayor cantidad de proyectos son: ～")
        for k in range(len(mayores)):
            print("\t \t～", mayores[k], end="\t～\t")
        print()
    else:
        print("\x1b[1;39m" + f"\t \t \t \t ～ El año con mayor cantidad de proyectos es:", mayores, "～")
        print()
