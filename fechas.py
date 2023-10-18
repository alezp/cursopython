#04from datetime import datetime, date
#fecha_cumple = input("Ingrese La fecha de su cumpleaños: ")
#fecha_actual = date.now().date()
#print(fecha_cumple)


from datetime import datetime

def calcular_tiempo_faltante(fecha_cumple):
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()

    # Convertir la fecha de cumpleaños a un objeto datetime
    fecha_cumple = datetime.strptime(fecha_cumple, "%d/%m/%Y").date()

    # Obtener el año actual y el año del próximo cumpleaños
    anio_actual = fecha_actual.year
    anio_proximo_cumple = fecha_cumple.replace(year=anio_actual)

    # Calcular la diferencia entre la fecha actual y el próximo cumpleaños
    if fecha_actual > anio_proximo_cumple:
        anio_proximo_cumple = fecha_cumple.replace(year=anio_actual + 1)

    tiempo_faltante = anio_proximo_cumple - fecha_actual

    # Imprimir el resultado
    print("Faltan {} días para tu próximo cumpleaños".format(tiempo_faltante.days))

# Solicitar la fecha de cumpleaños al usuario
fecha_cumple = input("Ingresa tu fecha de cumpleaños (dd/mm/aaaa): ")

# Calcular y mostrar el tiempo faltante para el próximo cumpleaños
calcular_tiempo_faltante(fecha_cumple)
