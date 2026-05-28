# Calculadora Científica y Graficadora en Consola

¡Bienvenido a la Calculadora Científica! Este es un programa hecho totalmente desde cero en Python. Te permite hacer desde sumas sencillas hasta cálculos avanzados y dibujar gráficas directamente en la pantalla de texto, todo sin necesidad de instalar programas o paquetes matemáticos extra.

## ¿Qué hace cada archivo?

Para mantener todo ordenado y fácil de entender, dividimos el proyecto en 5 archivos pequeños en lugar de uno gigante:

* **`operaciones_basicas.py`**: Se encarga de la matemática del día a día. Aquí están las funciones para sumar, restar, multiplicar, dividir y elevar números a una potencia.
* **`operaciones_cientificas.py`**: Es el cerebro. Calcula cosas más complejas como raíces cuadradas, factoriales, senos, cosenos y logaritmos. Todo esto se programó "a mano" usando fórmulas matemáticas que se repiten hasta dar con el resultado exacto.
* **`graficadora.py`**: Es la parte visual. Toma una función que tú inventes (como una línea o una curva) y la dibuja en la pantalla usando asteriscos (`*`) y rayitas para que puedas ver cómo se comporta.
* **`historial.py`**: Es como la memoria de la calculadora. Guarda automáticamente cada operación que haces para que puedas revisar tus resultados anteriores cuando quieras.
* **`main.py`**: Es el jefe del equipo. Este archivo junta a todos los demás y te muestra el menú principal en la pantalla. **Este es el único archivo que necesitas iniciar para que todo funcione.**

## ¿Cómo hacer funcionar el proyecto?

Hacer andar la calculadora es muy fácil. Solo sigue estos pasos:

1.  **Guarda todo junto:** Asegúrate de que los 5 archivos (`main.py`, `operaciones_basicas.py`, `operaciones_cientificas.py`, `graficadora.py` y `historial.py`) estén guardados dentro de la misma carpeta en tu computadora.
2.  **Abre tu consola:** Abre la terminal o consola de comandos de tu computadora (como el "Símbolo del sistema" en Windows o la "Terminal" en Mac/Linux).
3.  **Ve a la carpeta:** Usa tu consola para llegar a la carpeta donde guardaste los archivos.
4.  **Inicia el programa:** Escribe el siguiente comando y presiona la tecla Enter:
    `python main.py`
    *(Nota: Si usas Mac o Linux, es posible que debas escribir `python3 main.py`).*

## Instrucciones de uso

Una vez que el programa esté funcionando, verás un menú con 6 opciones en tu pantalla. Usarlo es como seguir una conversación:

1.  **Elige una opción:** Escribe el número de lo que quieres hacer (por ejemplo, el `1` para operaciones básicas) y presiona Enter.
2.  **Sigue las preguntas:** El programa te irá preguntando qué números quieres usar. Solo escríbelos y presiona Enter.
3.  **Para graficar (Opción 4):** El programa te preguntará qué tipo de línea o curva quieres dibujar y de qué tamaño quieres verla. Te recomendamos pedirle un rango pequeño (como desde el -10 hasta el 10) para que el dibujo quepa bien en tu pantalla y no se vea desordenado.
4.  **Revisa tus pasos:** Si eliges la opción `5`, podrás ver una lista con todas las cuentas que has hecho desde que abriste el programa.
5.  **Salir:** Cuando termines de usarla, solo elige la opción `6` para apagar la calculadora y cerrar el programa.
