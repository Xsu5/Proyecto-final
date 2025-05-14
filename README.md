# Proyecto-final
# PROYECTO: Método de Bisección en Python

# Este programa sirve para encontrar la raíz de una función usando el método de bisección.

# -----------------------
# ¿QUÉ HACE EL PROGRAMA?
# -----------------------
# - Te pide que escribas una función (por ejemplo: x**2 - 2 o math.sin(x)).
# - Luego te pide un intervalo (a y b) donde creas que está la raíz.
# - También te pide una tolerancia y cuántas veces intentar.
# - Te muestra paso por paso lo que hace hasta encontrar una raíz aproximada.

# -----------------------
# ¿CÓMO SE USA?
# -----------------------
# 1. Abre el archivo main.py en Visual Studio Code o en otro editor.
# 2. Corre el programa (F5 o desde terminal con `python main.py`).
# 3. Escribe la función que quieres usar.
# 4. Escribe los valores de a, b, la tolerancia y las iteraciones.
# 5. El programa te muestra los pasos y al final te dice la raíz aproximada.
# -----------------------
# ¿QUÉ MÉTODO USA?
# -----------------------
# Usa el Método de Bisección.

# Este método divide el intervalo por la mitad y busca dónde cambia de signo
# la función. Así se va acercando poco a poco a la raíz.

# -----------------------
# OTROS DATOS:
# -----------------------
# - No necesitas instalar nada extra.
# - Usa la librería "math" por si usas senos, cosenos, etc.
# - El código está hecho sencillo y con comentarios para entenderlo fácil.
# =======
# PROYECTO: Método de Bisección (Python)
# Autor: [ZEUS LEONARDO PENUELAS ARMENTA]
# Materia: Métodos Numéricos
# Fecha: Mayo 2025

# ------------------------------------------
# ¿QUÉ HACE ESTE PROGRAMA?
# ------------------------------------------
# Este programa permite encontrar una raíz aproximada de cualquier función matemática
# usando el Método de Bisección. 

# El usuario puede escribir la función que quiera (como x**2 - 2 o math.sin(x)),
# y el programa se encarga de aplicar el método paso a paso para hallar la raíz
# en un intervalo dado.

# ------------------------------------------
# INSTRUCCIONES DE USO:
# ------------------------------------------
# 1. Abre el archivo main.py en Visual Studio Code o cualquier editor.
# 2. Ejecuta el archivo.
# 3. Escribe la función que quieres analizar. Ejemplos:
#      - x**2 - 2
#      - x**3 - 4*x - 9
 #     - math.sin(x)
# 4. Ingresa los valores de a y b (los extremos del intervalo).
#    IMPORTANTE: f(a) y f(b) deben tener signos opuestos.
# 5. Ingresa la tolerancia (ejemplo: 0.001).
# 6. Ingresa el número máximo de iteraciones.

# El programa mostrará los pasos de cada iteración y al final la raíz aproximada.

# ------------------------------------------
# ¿QUÉ MÉTODO SE USÓ?
# ------------------------------------------
# Se usó el MÉTODO DE BISECCIÓN. Este método sirve para encontrar raíces de funciones
# reales continuas dentro de un intervalo [a, b].

# Lo que hace es ir dividiendo el intervalo por la mitad, y se queda con la mitad
# donde la función cambia de signo. Repite esto hasta que el valor sea suficientemente
# cercano a 0 o se llegue a la tolerancia deseada.

# Es un método fácil y confiable, aunque puede tardar varias iteraciones.

# ------------------------------------------
# REQUISITOS:
# ------------------------------------------
# - Tener Python instalado (versión 3.6 o superior).
# - Si usas funciones como math.sin(x), el módulo 'math' ya está importado.

# ------------------------------------------
# NOTAS FINALES:
# ------------------------------------------
# - El código está hecho de forma simple y clara.
# - No se usan librerías externas complicadas.
# - Ideal para entender cómo funciona el método paso a paso.

