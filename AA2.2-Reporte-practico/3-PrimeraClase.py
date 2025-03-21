# Programa de primer orden que imprime el nombre de un estudiante.
def obtener_nombre():
    return "Marcial Gamboa"
# El programa es de primer orden porque la función 
# obtener_nombre no recibe argumentos y retorna un 
# valor, en este caso el nombre del estudiante.
nombre_estudiante = obtener_nombre  # Asignamos la función a una variable
print(f"El nombre del estudiante es: {nombre_estudiante()}")
