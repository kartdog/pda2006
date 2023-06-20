# ejercicio - restaurant (tipo prueba)

import python_2006_val as fn
import numpy as np

lista_rut = []

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
        # incompleto, agregar filas para más facil asignacion
        print("El número es la cantidad de asientos en cada mesa.")
        for x in range(3):
            arreglo = np.array(lista_asientos)
            for y in range(3):
                arreglo = np.array(lista_asientos)
                for z in range(3):
                    arreglo = np.array(lista_asientos)
        print(arreglo)
    elif opcion == 2:
        # incompleto, agregar reserva con filas.
        print(">> Reservar mesa")
        rut = lista_rut.append(fn.val_rut())
        print(lista_rut)
        nombre = fn.val_nombre()
        correo = fn.val_correo()
        cantidad = fn.val_cantidad()
        if cantidad >= 1 and cantidad <= 2:
            print("Tiene disponible las mesas:")
            # incompleto, agregar para reservar las mesas.
            pass
        elif cantidad >= 1 and cantidad <= 4:
            print("Tiene disponible las mesas:")
            # incompleto, agregar para reservar las mesas.
            pass
        elif cantidad >= 1 and cantidad <= 6:
            print("Tiene disponible las mesas:")
            # incompleto, agregar para reservar las mesas.
            pass
        pass
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
                    # incompleto, agregar el monto total
                    for x in range(cantidad):
                        print("""
                        1. Jugo de naranja  $ 800
                        2.            Bilz  $ 1200
                        3.            Agua  $ 0
                        4.           Salir
                        """)
                        opcion_consumo = fn.val_opcion_con()
                        if opcion_consumo == 1:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 2:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 3:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        else:
                            pass
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
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 2:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 3:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        else:
                            pass                      
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
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 2:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        elif opcion_consumo == 3:
                            # incompleto, agregar para sumar opcion al costo total
                            pass
                        else:
                            pass
                elif opcion_carta == 4:
                    # incompleto, mostrar monto total, confirmar y volver al menú principal.
                    pass
                else:
                    break
        else:
            print("ERROR! rut no se encuentra registrado.")
    elif opcion == 4:
        # incompleto, agregar boleta, junto con el subtotal más el IVA, junto con descuento (?), y total.
        rut = fn.val_rut()
        if rut in lista_rut:
            pass
    elif opcion == 5:
        # incompleto, debe dejar disponible la mesa.
        rut = fn.val_rut()
        if rut in lista_rut:
            pass
    else:
        print("Gracias, adios.")
        break