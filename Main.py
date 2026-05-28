# main.py
import Operaciones_basicas as ob
import Operaciones_cientificas as oc
import Graficadora as gr
import Historial as ht

def mostrar_menu():
    print("\n--- CALCULADORA CIENTIFICA GRAFICADORA ---")
    print("1. Operaciones basicas")
    print("2. Operaciones cientificas")
    print("3. Evaluar una funcion personalizada")
    print("4. Graficar una funcion personalizada")
    print("5. Ver historial de operaciones")
    print("6. Salir")

def main():
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print("\n-- Operaciones Basicas --")
            print("1. Suma | 2. Resta | 3. Multiplicacion | 4. Division | 5. Potencia")
            sub_opcion = int(input("Opcion (1-5): "))
            
            if sub_opcion in [1, 2, 3, 4, 5]:
                a = float(input("Primer numero (o base): "))
                b = float(input("Segundo numero (o exponente): "))
                
                if sub_opcion == 1: res = ob.sumar(a, b); op = "Suma"
                elif sub_opcion == 2: res = ob.restar(a, b); op = "Resta"
                elif sub_opcion == 3: res = ob.multiplicar(a, b); op = "Multiplicacion"
                elif sub_opcion == 4: res = ob.dividir(a, b); op = "Division"
                elif sub_opcion == 5: res = ob.potencia(a, b); op = "Potencia"
                
                print(f"Resultado: {res}")
                ht.agregar(f"{op}: {a} con {b} = {res}")
            else:
                print("Opcion invalida.")

        elif opcion == 2:
            print("\n-- Operaciones Cientificas --")
            print("1. Factorial | 2. Raiz | 3. Exp | 4. Seno | 5. Coseno | 6. Ln")
            sub_opcion = int(input("Opcion (1-6): "))
            
            if sub_opcion in [1, 2, 3, 4, 5, 6]:
                x = float(input("Ingrese el numero: "))
                
                if sub_opcion == 1: res = oc.factorial(x); op = "Factorial"
                elif sub_opcion == 2: res = oc.raiz_cuadrada(x); op = "Raiz"
                elif sub_opcion == 3: res = oc.exponencial(x); op = "Exponencial"
                elif sub_opcion == 4: res = oc.seno(x); op = "Seno"
                elif sub_opcion == 5: res = oc.coseno(x); op = "Coseno"
                elif sub_opcion == 6: res = oc.logaritmo_natural(x); op = "Ln"
                
                print(f"Resultado: {res}")
                ht.agregar(f"{op} de {x} = {res}")
            else:
                print("Opcion invalida.")

        elif opcion == 3:
            formula, val, res = gr.evaluar()
            if formula != None:
                print(f"Resultado de evaluar f({val}): {res}")
                ht.agregar(f"Evaluo f(x)={formula} en x={val} -> {res}")

        elif opcion == 4:
            formula = gr.graficar()
            if formula != None:
                ht.agregar(f"Grafico funcion f(x)={formula} en consola")

        elif opcion == 5:
            ht.mostrar()

        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()