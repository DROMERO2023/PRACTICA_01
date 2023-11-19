# EJERCICIO 10 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario ingresar una lista (tal como lo solicita el ejercicio: Los Colores Rojo, Verde, Blanco, Negro, Rosa y Amarillo):

lista_original = input("Ingrese la lista separada por comas (por ejemplo, 'Rojo, Verde, Blanco, Negro, Rosa, Amarillo'): ").split(', ')

# PASO 02: Proceder a convertir la lista ingresada: De una lista de cadenas a una lista de elementos
lista_original = [elemento.strip() for elemento in lista_original]
# La función strip se utilizará para eliminar posibles espacios en blanco alrededor de los elementos ingresados por el usuario

# PASO 03: Se eliminarán los elementos en las posiciones 0, 4 y 5 (tomando en consideración la seperación de comas)
posiciones_a_eliminar = [0, 4, 5]
lista_resultante = [lista_original[i] for i in range(len(lista_original)) if i not in posiciones_a_eliminar]
# La función range se usará para crear una nueva lista que excluye los elementos en las posiciones especificadas

# PASO 04: Mostrar en Consola la lista resultante, eliminando las posiciones solicitadas: 0,4 y 5
print("Lista resultante, eliminando las posiciones 0, 4 y 5:", lista_resultante)
