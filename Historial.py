# historial.py

registro = []

def agregar(operacion_str):
    registro.append(operacion_str)

def mostrar():
    print("\n-- Historial de Operaciones --")
    if len(registro) == 0:
        print("El historial esta vacio.")
    else:
        for operacion in registro:
            print("-", operacion)