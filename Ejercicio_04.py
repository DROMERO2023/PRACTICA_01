# EJERCICIO 04 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario que ingrese un entero positivo
N = int(input("Ingrese un número entero positivo, N: "))

# PASO 02:  Es importante validar si el número ingresado es positivo, caso contrario se deberá solicitar al usuario ingresar un número entero positivo
if N <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:

# PASO 03: Luego de validar el número entero positivo, se procederá a calcular la suma de los enteros desde 1 hasta N
    suma_enteros = N * (N + 1) // 2

# PASO 04: Finalmente se mostrará en consola la suma de los enteros según la fórmula: n*(N+1)//2
    print("La suma de los enteros desde 1 hasta {} es: {}".format(N, suma_enteros))

