# operaciones_basicas.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(base, exponente):
    # Calcula la potencia usando un ciclo basico
    resultado = 1
    for i in range(int(exponente)):
        resultado = resultado * base
    return resultado