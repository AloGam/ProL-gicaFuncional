def cuadradosLista(arreglo):
    # Filtrar los enteros positivos y luego map para obtener sus cuadrados
    return list(map(lambda x: x**2, filter(lambda x: isinstance(x, int) and x > 0, arreglo)))

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)  # Salida: [25, 9]