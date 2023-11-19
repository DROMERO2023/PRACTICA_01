# EJERCICIO 03 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario la cantidad total de juguetes (payasos y muñecas) que se han vendido en el último pedido: 
total_payasos = int(input("Ingrese la cantidad total de payasos vendidos: "))
total_muñecas = int(input("Ingrese la cantidad total de muñecas vendidas: "))

# PASO 02: Valores en gramos definidos de la variable peso para cada tipo de producto (payasos y muñecas)
peso_payaso = 112  # en gramos
peso_muñeca = 75   # en gramos

# PASO 03: Calcular el peso total del paquete a ser enviado
peso_total = (total_payasos * peso_payaso) + (total_muñecas * peso_muñeca)

# PASO 04: Cálculo del peso total del paquete a ser enviado
print("El peso total del paquete es: {} gramos".format(peso_total))
