# EJERCICIO 08 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solcitar al usuario ingresar la hora en evaluación (en formato de 24 horas):
hora_evaluada = input("Ingrese la hora en formato de 24 horas (por ejemplo, 7:30): ")

# PASO 02: Haciendo uso del método de cadena SPLIT (para separar cadenas en subcadenas a partir de sus espacios y devolver una lista) se buscará obtener las horas y minutos:
horas, minutos = map(int, hora_evaluada.split(':')) # A través del map convertimos cada valor de la lista en enteros para luego asignarlos a las variables "Horas y Minutos"

# PASO 03: Convertir la hora a formato float para facilitar las comparaciones:
hora_final = horas + minutos / 60

# PASO 04: Definir los rangos de tiempo para el horario del desayuno, almuerzo y cena:
desayuno_inicio, desayuno_fin = 7.0, 8.0
almuerzo_inicio, almuerzo_fin = 12.0, 13.0
cena_inicio, cena_fin = 18.0, 19.0

# PASO 05: Evaluar horarios según valores ingresados, indicando si es hora de Desayunar, Almorzar, Cenar, o no es la Hora de Comer:
if desayuno_inicio <= hora_final <= desayuno_fin:
    print("Es hora de desayunar.")
elif almuerzo_inicio <= hora_final <= almuerzo_fin:
    print("Es hora de almorzar.")
elif cena_inicio <= hora_final <= cena_fin:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")
