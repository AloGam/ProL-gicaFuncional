# Programa de primer orden que calcula el promedio de un conjunto de calificaciones.
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)
# El programa es de primer orden porque la función calcular_promedio recibe como 
# argumento una lista de calificaciones y retorna un valor numérico, en este caso 
# el promedio de las calificaciones.
calificaciones = [85, 90, 78, 92]
promedio = calcular_promedio(calificaciones)
# La función calcular_promedio es de primer orden porque recibe y retorna valores.
# Es decir, es una función que recibe un argumento y retorna un valor.
print(f"El promedio de las calificaciones es: {promedio}")
