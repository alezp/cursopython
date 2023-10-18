class Academico:
  def __init__(self, nombre_institucion, alumnos):
    self.nombre_institucion = nombre_institucion
    self.alumnos = alumnos

  def promedio_general(self):
    lista_promedio_general = list()
    for alumno in self.alumnos:
      lista_promedio_general.append(
          alumno.obtener_promedio_general()
      )
    return sum(lista_promedio_general) // len(lista_promedio_general)

  def alumnos_graduados(self,aprueba_con):
    lista_alumnos_graduados = list()
    for alumno in self.alumnos:
      if not alumno.materias_desaprobadas(aprueba_con):#=> una lista vacía es == a None o a False
        print(alumno.nombre)
        lista_alumnos_graduados.append(alumno.nombre)
    return lista_alumnos_graduados