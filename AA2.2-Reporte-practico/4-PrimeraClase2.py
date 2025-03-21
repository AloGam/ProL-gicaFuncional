# Programa de primer orden que calcula el área de un círculo.
def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)
# El programa es de primer orden porque la función 
# calcular_area_circulo recibe como argumento el radio de un círculo
# y retorna un valor numérico, en este caso el área del círculo.
area_funcion = calcular_area_circulo  # Asignamos la función a una variable
area = area_funcion(5)  # Llamamos a la función a través de la variable
print(f"El área del círculo es: {area}")
