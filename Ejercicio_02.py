# EJERCICIO 02 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario el costo de la comida y el porcentaje de propina que desea dejar (mayor o igual al 15%)
consumo_en_dolares = float(input("Ingrese el costo de su comida: $"))
porcentaje_de_propina = float(input("Ingrese el porcentaje de propina que desea dejar (mayor o igual al 15%): "))

# PASO 02: Calcular la cantidad de propina según el valor del consumo:
propina = (porcentaje_de_propina / 100) * consumo_en_dolares 

# PASO 03: Mostrar la cantidad de propina
print("La cantidad de propina a dejar es: ${}".format(propina))