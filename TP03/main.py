from funciones import *

def principal():
    op = None
    n = 0
    c1 = 0
    v = [0]
    paso_1 = paso_5 = False
    while op != 8:
        op = menu()
        if op == 1:
            v = crear_vector(v, c1)
            c1 += 1
            paso_1 = True
        elif op == 2 and paso_1:
            seleccion_directa(v)
            write_punto_2(v)
        elif op == 3 and paso_1:
            punto_3(v)
        elif op == 4 and paso_1:
            punto_4(v)
        elif op == 5 and paso_1:
            contadores = punto_5(v)
            paso_5 = True
        elif op == 6 and paso_1:
            print()
            print("\x1b[1;39m" + "\t \t \t \t ～～～～～～ OPCIONES ～～～～～～ ")
            print("\t \t \t \t 00-Python, 01-Java, 02-C++, 03-Javascript, 04-Shell")
            print("\t \t \t \t 05-HTML 06-Ruby 07-Swift, 08-C#, 09-VB, 10-Go")
            punto_6(v)
        elif op == 7 and paso_1 and paso_5:
            punto_7(contadores, v)
    print("\x1b[1;32m" + "\t \t \t \t ～ Selecciono SALIR.....ADIOS! ～")
    print( '-_'*10+'FIN DEL PROGRAMA'+'-_'*10)

if __name__ == '__main__':
    principal()
