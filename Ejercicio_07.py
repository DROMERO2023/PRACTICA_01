# EJERCICIO 07 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario el ingreso de dos (02) números:

valor_numero_01 = float(input("Ingrese el primer número : "))
valor_numero_02 = float(input("Ingrese el segundo número: "))

# PASO 02: Solicitar al usuario la selección de un determinado Menú de Opciones
print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")

# PASO 03: Validar la selección del valor del Menú de Opciones:
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

# PASO 04: Ejecutar las operaciones según valor del Menú de Opciones seleccionado, si es una opción que no pertenece al Menú deberá indicarse como selección inválida:
if opcion == '1':
    resultado = int(valor_numero_01 + valor_numero_02)
    print("La suma de {} y {} es: {}".format(valor_numero_01, valor_numero_02, resultado))
elif opcion == '2':
    resultado = int(valor_numero_01 - valor_numero_02)
    print("La resta de {} y {} es: {}".format(valor_numero_01, valor_numero_02, resultado))
elif opcion == '3':
    resultado = int(valor_numero_01 * valor_numero_02)
    print("La multiplicación de {} y {} es: {}".format(valor_numero_01, valor_numero_02, resultado))
else:
    print("Opción inválida. Por favor, seleccione un valor predeterminado del Menú de Opciones: 1, 2 o 3.")
