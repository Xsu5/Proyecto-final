import math

# Evaluar función escrita por el usuario
def funcion(x, expresion):
    return eval(expresion)

# Método de Bisección
def biseccion(a, b, tolerancia, max_iteraciones, expresion):
    pasos = []

    if funcion(a, expresion) * funcion(b, expresion) >= 0:
        print("f(a) y f(b) deben tener signos opuestos.")
        return None, pasos

    iteracion = 0
    while (b - a) / 2 > tolerancia and iteracion < max_iteraciones:
        c = (a + b) / 2
        pasos.append((iteracion + 1, a, b, c, funcion(c, expresion)))

        if funcion(c, expresion) == 0:
            break
        elif funcion(a, expresion) * funcion(c, expresion) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    return c, pasos

# INICIO DEL PROGRAMA
print("Método de Bisección - Versión Genérica")
print("Escribe la función en Python. Ejemplos:")
print("  x**2 - 2")
print("  math.sin(x)")
print("  x**3 - 4*x - 9\n")

# Pedimos datos
expresion = input("Ingresa la función f(x): ")
a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
tolerancia = float(input("Ingresa tolerancia: "))
max_iteraciones = int(input("Ingresa número máximo de iteraciones: "))

# Ejecutamos
raiz, pasos = biseccion(a, b, tolerancia, max_iteraciones, expresion)

# Mostramos resultados
print("\nPasos:")
print("Iteración\t a\t\t b\t\t c\t\t f(c)")
for p in pasos:
    print(f"{p[0]}\t\t {p[1]:.6f}\t {p[2]:.6f}\t {p[3]:.6f}\t {p[4]:.6f}")

# Resultado final
if raiz:
    print(f"\nRaíz aproximada: {raiz:.6f}")
