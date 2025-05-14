# Proyecto-final
PROYECTO: Método de Bisección (Python)
Autor: [Tu nombre]
Materia: Métodos Numéricos
Fecha: Mayo 2025

------------------------------------------
¿QUÉ HACE ESTE PROGRAMA?
------------------------------------------
Este programa permite encontrar una raíz aproximada de cualquier función matemática
usando el Método de Bisección. 

El usuario puede escribir la función que quiera (como x**2 - 2 o math.sin(x)),
y el programa se encarga de aplicar el método paso a paso para hallar la raíz
en un intervalo dado.

------------------------------------------
INSTRUCCIONES DE USO:
------------------------------------------
1. Abre el archivo main.py en Visual Studio Code o cualquier editor.
2. Ejecuta el archivo.
3. Escribe la función que quieres analizar. Ejemplos:
     - x**2 - 2
     - x**3 - 4*x - 9
     - math.sin(x)
4. Ingresa los valores de a y b (los extremos del intervalo).
   IMPORTANTE: f(a) y f(b) deben tener signos opuestos.
5. Ingresa la tolerancia (ejemplo: 0.001).
6. Ingresa el número máximo de iteraciones.

El programa mostrará los pasos de cada iteración y al final la raíz aproximada.

------------------------------------------
¿QUÉ MÉTODO SE USÓ?
------------------------------------------
Se usó el MÉTODO DE BISECCIÓN. Este método sirve para encontrar raíces de funciones
reales continuas dentro de un intervalo [a, b].

Lo que hace es ir dividiendo el intervalo por la mitad, y se queda con la mitad
donde la función cambia de signo. Repite esto hasta que el valor sea suficientemente
cercano a 0 o se llegue a la tolerancia deseada.

Es un método fácil y confiable, aunque puede tardar varias iteraciones.

------------------------------------------
REQUISITOS:
------------------------------------------
- Tener Python instalado (versión 3.6 o superior).
- Si usas funciones como math.sin(x), el módulo 'math' ya está importado.

------------------------------------------
NOTAS FINALES:
------------------------------------------
- El código está hecho de forma simple y clara.
- No se usan librerías externas complicadas.
- Ideal para entender cómo funciona el método paso a paso.

