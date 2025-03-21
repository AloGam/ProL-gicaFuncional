# Programa lambda que calcula el promedio de un conjunto de calificaciones aprovadas.
calificaciones = [85, 90, 72, 92, 69]
# La función lambda es una función anónima que se puede usar 
# en lugar de una función normal. En este caso, se usa para 
# filtrar las calificaciones aprobadas.   
calif_aprobadas = list(filter(lambda x: x >= 75, calificaciones))
print(f"Calificaciones aprobadas: {calif_aprobadas}")
# La función filter recibe dos argumentos: una función y una lista.
# La función lambda recibe un argumento y retorna True si el argumento
# es mayor o igual a 80, en caso contrario retorna False.
# La función filter retorna una lista con los elementos de la lista
# original que cumplen con la condición de la función lambda.
