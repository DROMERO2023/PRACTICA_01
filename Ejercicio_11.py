# EJERCICIO 11 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario el ingreso de una lista (con datos duplicados), el método SPLIT permité ingresar un delimitador específico en este caso la coma (,)
lista_original = input("Ingrese un listado de números separados por comas (asegúrese de ingresar un espacio por cada valor ingresado, por ejemplo, '1, 1, 2, 3, 4, 4, 5, 1'): ").split(', ')

# PASO 02: Convertir la lista de cadenas a una lista de enteros, el método STRIP permitirá eliminar espacios en blanco al principio y al final de la cadena de texsto
lista_original = [int(elemento.strip()) for elemento in lista_original]

# PASO 03: Crear una lista sin duplicados usando el método SET (permite solo disponer de elementos únicos)
lista_sin_duplicados = list(set(lista_original))

# PASO 04: Mostrar en consola la lista resultante sin valores duplicados:
print("Lista sin duplicados:", lista_sin_duplicados)
