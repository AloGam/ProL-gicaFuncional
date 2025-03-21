# segundo programa de primer orden que cuenta la cantidad de asignaturas en una lista.
def contar_asignaturas(asignaturas):
    return len(asignaturas)
# El programa es de primer orden porque la función contar_asignaturas recibe como argumento una lista 
# de asignaturas y retorna un valor numérico, en este caso la cantidad de asignaturas en la lista.
asignaturas = ["Matemáticas", "Programación", "Redes", "Base de Datos", "Ingles"]
# La función contar_asignaturas es de primer orden porque recibe y retorna valores, es decir, es una 
# función que recibe un argumento y retorna un valor.
total_asignaturas = contar_asignaturas(asignaturas)
# En este caso, la función contar_asignaturas recibe una lista de asignaturas y retorna la cantidad 
# de asignaturas en la lista.
print(f"Total de asignaturas: {total_asignaturas}")
