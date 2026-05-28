# operaciones_cientificas.py
from Operaciones_basicas import potencia

def factorial(n):
    if n < 0:
        return "Error: Factorial negativo no definido"
    resultado = 1
    for i in range(1, int(n) + 1):
        resultado = resultado * i
    return resultado

def raiz_cuadrada(x):
    if x < 0:
        return "Error: Raiz de numero negativo"
    if x == 0:
        return 0.0
    aproximacion = x / 2.0
    for i in range(20): 
        aproximacion = (aproximacion + x / aproximacion) / 2.0
    return aproximacion

def exponencial(x):
    resultado = 0.0
    for i in range(15):
        resultado += potencia(x, i) / factorial(i)
    return resultado

def seno(x):
    resultado = 0.0
    for i in range(10): 
        signo = potencia(-1, i)
        exponente = 2 * i + 1
        termino = signo * (potencia(x, exponente) / factorial(exponente))
        resultado += termino
    return resultado

def coseno(x):
    resultado = 0.0
    for i in range(10): 
        signo = potencia(-1, i)
        exponente = 2 * i
        termino = signo * (potencia(x, exponente) / factorial(exponente))
        resultado += termino
    return resultado

def logaritmo_natural(x):
    if x <= 0:
        return "Error: Logaritmo de numero cero o negativo"
    resultado = 0.0
    termino_base = (x - 1) / (x + 1)
    for i in range(20):
        exponente = 2 * i + 1
        termino = (1 / exponente) * potencia(termino_base, exponente)
        resultado += termino
    return 2 * resultado