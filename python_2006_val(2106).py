# validaciones.


def val_rut():
    while True:
        try:
            rut = int(input("Ingrese rut (sin digito verificador, ni puntos): "))
            if rut >= 1000000 or rut <= 99999999:
                return rut
            else:
                print("ERROR! ingrese rut válido.")
        except:
            print("ERROR! ingrese un número entero.")

# agregar "sin espacios"
def val_nombre():
    while True:
        nombre = input("Ingrese nombre (min. 3 letras): ")
        if len(nombre) > 3:
            return nombre
        else:
            print("ERROR! ingrese un nombre válido.")

def val_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! ingrese un correo válido.")

def val_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción (1-6): "))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! ingrese una opción válida.")

        except:
            print("ERROR! ingrese un número entero.")

def val_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas (1-6): "))
            if cantidad in (1,2,3,4,5,6):
                return cantidad
            else:
                print("ERROR! ingrese una cantidad válida")
        except:
            print("ERROR! ingrese un número entero.")

def val_carta():
    while True:
        try:
            opcion_carta = int(input("Ingrese opción (1-5): "))
            if opcion_carta in (1,2,3,4,5):
                return opcion_carta
            else:
                print("ERROR! ingrese una opción válida.")
        except:
            print("ERROR! ingrese un número entero.")

def val_opcion_con():
    while True:
        try:
            opcion_consumo = int(input("Ingrese opción (1-3): "))
            if opcion_consumo in (1,2,3,4):
                return opcion_consumo
            else:
                print("ERROR! ingrese una opción válida.")
        except:
            print("ERROR! ingrese un número entero.")

def val_columna():
    while True:
        try:
            opcion_columna = int(input("Elija la columna en que sentarse (Si tiene una 'x' esta ocupada): "))
            if opcion_columna in (1,2,3):
                return opcion_columna
            else:
                print("ERROR! elija una opción válida.")
        except:
            print("ERROR! debe ingresar un número entero.")

def val_fila():
    while True:
        try:
            opcion_fila = int(input("Elija la fila en la que sentarse (Si tiene una 'x' esta ocupada): "))
            if opcion_fila in (1,2,3):
                return opcion_fila
            else:
                print("ERROR! elija una opción válida.")
        except:
            print("ERROR! debe ingresar un número entero.")