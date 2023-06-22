# ejercicio - restaurant (tipo prueba)

import python_2006_val as fn
import numpy as np

total = 0
subtotal = 0
acum = 0

lista_rut = []
lista_fila = []
lista_columna = []
lista_asientos = [[2,2,2],
                  [4,4,4],
                  [6,6,6]]

while True:
    print(""" MENÚ
    1. Ver restaurant
    2.  Reservar mesa
    3.          Carta
    4.          Pagar
    5.       Cancelar
    6.          Salir
    """)

    opcion = fn.val_opcion()

    if opcion == 1:
        print("Cada número representa una mesa y la cantidad de asientos en ella: ")
        num = 1
        for x in range(3):
            acum += num
            print(acum, "", end="")
            for y in range(3):
                print("",lista_asientos[x][y], end="")
            print()
        print(" "," 1-2-3")

    elif opcion == 2:
        print(">> Reservar mesa")
        rut = lista_rut.append(fn.val_rut())
        nombre = fn.val_nombre()
        correo = fn.val_correo()
        cantidad = fn.val_cantidad()
        if cantidad == 2:
            num = 1
            for x in range(3):
                acum += num
                print(acum, "",end="")
                for y in range(3):
                        print("",lista_asientos[x][y], end="")
                print()
            print("   1 2 3")
            while True:
                fila = fn.val_fila()
                columna = fn.val_columna()
                if lista_asientos[fila-1][columna-1] == 'X':
                    print("ERROR! mesa ocupada, elija otra opción.")
                else:
                    original_val = lista_asientos[fila-1][columna-1]
                    lista_asientos[fila-1][columna-1] = 'X'
                    print("Mesa reservada.")
                    print(original_val)
                    index_fila = fila - 1
                    index_columna = columna - 1
                    lista_fila.append(index_fila)
                    lista_columna.append(index_columna)
                    break            
        elif cantidad in (3,4):
            acum = 1
            num = 1
            for x in lista_asientos[1:3]:
                acum += num 
                print(acum, "", end = "")
                print(*x)
            print("  1 2 3")
            while True:
                fila = fn.val_fila()
                columna = fn.val_columna()
                if lista_asientos[fila-1][columna-1] == 'X':
                    print("ERROR! mesa ocupada, elija otra opción.")
                else:
                    lista_asientos[fila-1][columna-1] = 'X'
                    print("Mesa reservada.")
                    break
        else:
            for x in lista_asientos[2:3]:
                print("3", "", end = "")
                print(*x)
            print("  1 2 3")
            while True:
                fila = 2
                columna = fn.val_columna()
                if lista_asientos[fila-1][columna-1] == 'X':
                    print("ERROR! mesa ocupada, elija otra opción.")
                else:
                    lista_asientos[fila-1][columna-1] = 'X'
                    print("Mesa reservada.")
                    break
    elif opcion == 3:
        rut = fn.val_rut()
        if rut in lista_rut:
            while True: 
                print("""CARTA
                1. Bebestibles
                2.      Platos
                3.     Postres
                4.       Pedir
                5.    Cancelar
                """)

                opcion_carta = fn.val_carta()
                if opcion_carta == 1:
                        for x in range(cantidad):
                            print("""
                            1. Jugo de naranja  $ 800
                            2.            Bilz  $ 1200
                            3.            Agua  $ 0
                            4.           Salir
                            """)
                            opcion_consumo = fn.val_opcion_con()
                            if opcion_consumo == 1:
                                subtotal += 800
                            elif opcion_consumo == 2:
                                subtotal += 1200
                            elif opcion_consumo == 3:
                                subtotal += 0
                            else:
                                break
                elif opcion_carta == 2:
                        for x in range(cantidad):
                            print("""
                            1.        Puré con vienesas $ 2500
                            2. Fideos con salsa & carne $ 2000
                            3.  Arroz con pollo al jugo $ 2750
                            4.           Salir
                            """)
                            opcion_consumo = fn.val_opcion_con()
                            if opcion_consumo == 1:
                                subtotal += 2500
                            elif opcion_consumo == 2:
                                subtotal += 2000
                            elif opcion_consumo == 3:
                                subtotal += 2750
                            else:
                                break                    
                elif opcion_carta == 3:
                        for x in range(cantidad):
                            print("""
                            1.     Brazo de reina   $ 1250
                            2.       Pie de limon   $ 1500
                            3. Helado de vainilla   $ 1000
                            4.           Salir
                            """)
                            opcion_consumo = fn.val_opcion_con()
                            if opcion_consumo == 1:
                                subtotal += 1250
                            elif opcion_consumo == 2:
                                subtotal += 1500
                            elif opcion_consumo == 3:
                                subtotal += 1000
                            else:
                                break
                elif opcion_carta == 4:
                    print("Usted lleva $", subtotal,"en su pedido.")
                    break
                else:
                    print("Se cancela el pedido")
                    subtotal = 0
                    break
        else:
            print("ERROR! rut no se encuentra registrado.")
    elif opcion == 4:
        rut = fn.val_rut()
        if rut in lista_rut:
            print("BOLETA")
            print("Subtotal :", subtotal)
            print("IVA (19%):",(subtotal * 0.19))
            print("Descuento: 0%")
            print("Total    :", (subtotal + (subtotal * 0.19)))
    elif opcion == 5:
        rut = fn.val_rut()
        if rut in lista_rut:
            index_rut = lista_rut.index(rut)
            index_pos = index_rut
            postotal = lista_asientos[index_pos][index_pos]
            lista_asientos[index_pos][index_pos] = original_val
            print("Se cancela reserva, mesa queda disponible.")       
    else:
        print("Gracias, adios.")
        break