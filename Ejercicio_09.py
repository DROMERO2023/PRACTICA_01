# EJERCICIO 09 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario ingresar una Lista de palabras, separadas por comas:
lista_original = input("Ingrese la lista separada por comas (por ejemplo, 'Di, buen, día, a, papa'): ").split(', ')
# El método Split, permitirá convertir los textos ingresados en una Lista

# PASO 02: Según los valores de la lsita anterior, se procederá a invertir la lista haciendo uso del método Slicing: 
lista_invertida = lista_original[::-1] # El método Slicing, permitirá seleccionar un subconjunto de elementos de una secuencia, como una lista o cadena

# PASO 02: Se mostrará en consola tanto la Lista Original como la Lista Invertida
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
