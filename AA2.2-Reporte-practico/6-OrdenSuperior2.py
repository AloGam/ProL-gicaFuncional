# Programa de orden superior que crea una función multiplicadora.
def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar
# El programa es de orden superior porque la función crear_multiplicador
# retorna una función, en este caso la función multiplicar, que multiplica
# un valor por el factor que se le pasó a la función crear_multiplicador.
doble = crear_multiplicador(2)  # Devuelve una función que multiplica por 2
resultado = doble(10)

print(f"El doble de 10 es: {resultado}")
