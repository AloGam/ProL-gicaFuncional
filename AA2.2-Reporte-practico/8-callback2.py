# Programa con funcion callback que filtra estudiantes aprobados y excelentes.
def filtrar_estudiantes(calificaciones, criterio):
    # Esta función toma una lista de calificaciones 
    # y una función de criterio (callback).
    return [cal for cal in calificaciones if criterio(cal)]
    # Filtra las calificaciones según el criterio y devuelve 
    # una lista de calificaciones que cumplen con el criterio.

def aprobado(calificacion):
    # Función que determina si una calificación es aprobada (mayor o igual a 60).
    return calificacion >= 70

def excelente(calificacion):
    # Función que determina si una calificación es excelente (mayor o igual a 90).
    return calificacion >= 90

# Lista de calificaciones de estudiantes
calificaciones = [55, 78, 90, 45, 88, 92, 67]

# Filtrar estudiantes aprobados usando la función callback 'aprobado'
estudiantes_aprobados = filtrar_estudiantes(calificaciones, aprobado)
print(f"Estudiantes aprobados: {estudiantes_aprobados}")

# Filtrar estudiantes excelentes usando la función callback 'excelente'
estudiantes_excelentes = filtrar_estudiantes(calificaciones, excelente)
print(f"Estudiantes excelentes: {estudiantes_excelentes}")
