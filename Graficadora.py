# graficadora.py
from Operaciones_basicas import potencia

tipos_funciones = {
    1: "Lineal (f(x) = m*x + b)",
    2: "Cuadratica (f(x) = a*x^2 + b*x + c)",
    3: "Cubica (f(x) = a*x^3 + b*x^2 + c*x + d)"
}

def formatear_signo(numero):
    if numero < 0:
        return f"- {numero * -1}" 
    else:
        return f"+ {numero}"

def pedir_coeficientes():
    print("\n--- Construye tu propia Funcion ---")
    for clave, valor in tipos_funciones.items():
        print(f"{clave}. {valor}")
        
    tipo = int(input("Seleccione el tipo de funcion (1-3): "))
    
    a, b, c, d = 0.0, 0.0, 0.0, 0.0
    formula_texto = ""
    
    if tipo == 1:
        m = float(input("Ingrese la pendiente (m): "))
        b_val = float(input("Ingrese el intercepto (b): "))
        c, d = m, b_val
        formula_texto = f"{m}*x {formatear_signo(b_val)}"
        
    elif tipo == 2:
        a_val = float(input("Ingrese el coeficiente a (x^2): "))
        b_val = float(input("Ingrese el coeficiente b (x): "))
        c_val = float(input("Ingrese el termino constante c: "))
        b, c, d = a_val, b_val, c_val
        formula_texto = f"{a_val}*x^2 {formatear_signo(b_val)}*x {formatear_signo(c_val)}"
        
    elif tipo == 3:
        a = float(input("Ingrese el coeficiente a (x^3): "))
        b = float(input("Ingrese el coeficiente b (x^2): "))
        c = float(input("Ingrese el coeficiente c (x): "))
        d = float(input("Ingrese el termino constante d: "))
        formula_texto = f"{a}*x^3 {formatear_signo(b)}*x^2 {formatear_signo(c)}*x {formatear_signo(d)}"
        
    else:
        print("Tipo de funcion no valida.")
        return None, None, None, None, None
        
    return a, b, c, d, formula_texto

def calcular_polinomial(x, a, b, c, d):
    termino3 = a * potencia(x, 3)
    termino2 = b * potencia(x, 2)
    termino1 = c * x
    termino0 = d
    return termino3 + termino2 + termino1 + termino0

def graficar_ascii_dinamico(a, b, c, d, x_min, x_max, ancho=80, alto=24, mostrar_ejes=True):
    if ancho < 10 or alto < 10:
        print("Error: dimensiones muy pequenas")
        return
    if x_min >= x_max:
        print("Error: x_min debe ser menor que x_max")
        return

    # 1. Calcular todos los puntos de Y usando listas basicas
    puntos_y = [] 
    for i in range(ancho):
        x = x_min + (i * (x_max - x_min) / (ancho - 1))
        y = calcular_polinomial(x, a, b, c, d)
        puntos_y.append(y)

    y_min = min(puntos_y)
    y_max = max(puntos_y)

    if y_min == y_max:
        y_min -= 1
        y_max += 1

    # 2. Crear la matriz vacia
    matriz = []
    for fila in range(alto):
        linea = []
        for columna in range(ancho):
            linea.append(" ")
        matriz.append(linea)

    # 3. Dibujar Eje Y (|)
    if mostrar_ejes and (x_min <= 0 <= x_max):
        col_y = int((0 - x_min) / (x_max - x_min) * (ancho - 1))
        for fila in range(alto):
            matriz[fila][col_y] = "|"

    # 4. Dibujar Eje X (-)
    if mostrar_ejes and (y_min <= 0 <= y_max):
        fila_x = int((y_max - 0) / (y_max - y_min) * (alto - 1))
        for col in range(ancho):
            if matriz[fila_x][col] == "|":
                matriz[fila_x][col] = "+"
            else:
                matriz[fila_x][col] = "-"

    # 5. Dibujar la funcion con asteriscos usando un ciclo basico
    for i in range(len(puntos_y)):
        y = puntos_y[i]
        fila = int((y_max - y) / (y_max - y_min) * (alto - 1))
        
        if fila >= 0 and fila < alto:
            matriz[fila][i] = "*"
   
    # 6. Mostrar la grafica concatenando a mano
    print("\n        GRAFICA        \n")
    for fila in matriz:
        texto_fila = ""
        for caracter in fila:
            texto_fila += caracter
        print(texto_fila)

def graficar():
    a, b, c, d, formula = pedir_coeficientes()
    if formula is None:
        return None
        
    print("\n--- Configuracion del Rango ---")
    x_min = float(input("Ingrese x minimo (ej. -10): "))
    x_max = float(input("Ingrese x maximo (ej. 10): "))

    print(f"\n--- Graficando f(x) = {formula} ---")
    # Forzamos un tamaño más pequeño para que no se desborde en la consola
    graficar_ascii_dinamico(a, b, c, d, x_min, x_max, ancho=50, alto=20)
        
    return formula

def evaluar():
    a, b, c, d, formula = pedir_coeficientes()
    if formula is None:
        return None, None, None
        
    val = float(input("Ingrese el valor especifico de X para evaluar: "))
    res = calcular_polinomial(val, a, b, c, d)
    return formula, val, res