# EJERCICIO 06 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Con fines de validación, se deberá solicitar la edad del cliente (usuario de sala de juego)
edad_cliente = int(input("Ingrese la edad del cliente: "))

# PASO 02: En función a la edad ingresada, se calculará el precio de la entrada (según política de edades de la empresa)
if edad_cliente < 4:
    precio_entrada = 0  # Política Empresa: Menores de 4 años entran gratis
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # Política Empresa: :Clientes de 4 a 18 años pagan $5
else:
    precio_entrada = 10  # Política Empresa: Clientes mayores de 18 años pagan $10

# PASO 03: Mostrar en consola el precio de la entrada, según condicionales de rango de edades y políticas de precios
print("Según la edad del cliente, el precio de la entrada es: ${}".format(precio_entrada))
