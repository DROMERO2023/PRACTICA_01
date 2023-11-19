# EJERCICIO 05 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario ingresar la cantidad de veces a las que asistió a un show musical (durante el último año)

cantidad_shows = int(input("Ingrese la cantidad de shows musicales a las que ha asistido en el último año: "))

# PASO 02: Proceder a validar si el valor ingresado es mayor o igual a 03 Shows Musicales
validacion_shows = cantidad_shows > 3

# PASO 03: Mostrar el resultado en valores BOOLEANOS: TRUE o FALSE
print("¿Ha visto más de 3 shows musicales en el último año?: {}".format(validacion_shows))
